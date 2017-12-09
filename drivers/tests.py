from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from .models import Driver


class DriverTest(TestCase):
    def create_driver(self, full_name="Test", gender="yes", pesel="132456789", permissions_level=1, phone_number=2):
        return Driver.objects.create(
            full_name=full_name,
            gender=gender,
            pesel=pesel,
            permissions_level=permissions_level,
            phone_number=phone_number
        )

    def test_read(self):
        w = self.create_driver()
        d = Driver.objects.get(id=w.id)
        self.assertEqual(d, w)

    def test_driver_creation(self):
        w = self.create_driver()
        self.assertTrue(isinstance(w, Driver))
        self.assertEqual(w.gender, 'yes')
        self.assertEqual(w.phone_number, 2)
        self.assertEqual(w.permissions_level, 1)

    def test_driver_update(self):
        d1 = self.create_driver()

        fields = ['full_name', 'gender', 'pesel', 'permissions_level', 'phone_number']

        d1.phone_number = 33
        d1.gender = 'Apache'
        d1.pesel = '6546546'
        d1.full_name = "grzesiek jestem"
        d1.permissions_level = 2

        d2 = Driver.objects.get(id=d1.id)

        for i in fields:
            self.assertNotEqual(str(d1.__getattribute__(i)), str(d2.__getattribute__(i)))

        d1.save()
        d3 = Driver.objects.get(id=d1.id)

        for i in fields:
            self.assertEqual(str(d1.__getattribute__(i)), str(d3.__getattribute__(i)))

    def test_delete(self):
        d1 = self.create_driver()
        id = d1.id
        d1.delete()

        error_occured = False
        try:
            d2 = Driver.objects.get(id=id)
        except ObjectDoesNotExist:
            error_occured = True

        self.assertTrue(error_occured)


# coding: utf-8
from django.test import TestCase
from .forms import DriverBasicForm
import random


def phone_gen(x, formater= '{}-{}-{}'):
    for i in range(x):
        x,y,z = random.randint(100,999),random.randint(100,999),random.randint(100,999)
        yield formater.format(x,y, z)

class FormTests(TestCase):
    def test_basic_form(self):
        form_data = {'full_name': 'Adamiak Adam', 'gender': 'male', 'pesel': '55011156916', 'phone_number': '123123123',
                     'permissions_level': 'C+E'}
        form = DriverBasicForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_permission(self):
        form_data = {'full_name': 'Adamiak Adam', 'gender': 'male', 'pesel': '55011156916', 'phone_number': '123123123',
                     'permissions_level': 'niematakichpermi'}

        form = DriverBasicForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['permissions_level'][0],
                          'Select a valid choice. niematakichpermi is not one of the available choices.')

        ok_perm = ['AM', 'A', 'A1', 'A2', 'B', 'B+E', 'C', 'C+E', 'C1', 'C1+E', 'D', 'D+E', 'D1', 'D1+E']
        for i in ok_perm:
            form_data['permissions_level'] = i
            form = DriverBasicForm(data=form_data)
            self.assertTrue(form.is_valid())

    def test_phone(self):
        form_data = {'full_name': 'Adamiak Adam', 'gender': 'male', 'pesel': '55011156916',
                     'phone_number': '1234567890',
                     'permissions_level': 'C+E'}
        form = DriverBasicForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['phone_number'][0], 'Phone number is in bad format')

        for i in phone_gen(100):
            form_data['phone_number'] = i
            form = DriverBasicForm(data=form_data)
            self.assertTrue(form.is_valid())

        for i in phone_gen(100, formater='{}{}{}'):
            form_data['phone_number'] = i
            form = DriverBasicForm(data=form_data)
            self.assertTrue(form.is_valid())

        for i in phone_gen(100, formater='{}.{}.{}'):
            form_data['phone_number'] = i
            form = DriverBasicForm(data=form_data)
            self.assertTrue(form.is_valid())

        form_data['phone_number']= '666-666-666'
        form = DriverBasicForm(data=form_data)
        self.assertTrue(form.is_valid())

        # self.assertEquals(form.errors['phone_number'][0], 'Phone number is in bad format')

    def test_gender(self):
        form_data = {'full_name': 'Adamiak Adam', 'gender': 'male', 'pesel': '55011156916', 'phone_number': '123123123',
                     'permissions_level': 'C+E'}

        form = DriverBasicForm(data=form_data)
        self.assertTrue(form.is_valid())

        form_data['gender'] = 'niematakiejplci'
        form = DriverBasicForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['gender'][0], 'Gender is in bad format')

        ok_gender = ['m', 'f', 'k', 'apache helicopter', 'man', 'female', 'male', 'women', 'kobieta', 'mężczyzna', 'mezczyzna', 'other', 'inne']

        for i in ok_gender:
            form_data['gender'] = i
            form = DriverBasicForm(data=form_data)
            self.assertTrue(form.is_valid())


    def test_pesel(self):
        form_data = {'full_name': 'Adamiak Adam', 'gender': 'male', 'pesel': '55011156916', 'phone_number': '123123123',
                     'permissions_level': 'C+E'}

        form = DriverBasicForm(data=form_data)
        self.assertTrue(form.is_valid())

        form_data['pesel'] = 'zadlugipeseltojest'
        form = DriverBasicForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['pesel'][0], 'Ensure this value has at most 11 characters (it has 18).')

        bad_pesels = ['niema', '5646549879', '05060650503', 'alesochodzi']
        for i in bad_pesels:
            form_data['pesel'] = i
            form = DriverBasicForm(data=form_data)
            self.assertFalse(form.is_valid())
            self.assertEquals(form.errors['pesel'][0], 'Pesel is in bad format')

        ok_pesels = ['56041813149', '00252156137', '74062049617', '76082114616', '95092348486', '82061226663',
                     '87110827264', '01271224881', '93040475291', '60022088433', '64080722267', '86073191874',
                     '93010767953', '54073032138', '89101082911']
        for i in ok_pesels:
            form_data['pesel'] = i
            form = DriverBasicForm(data=form_data)
            self.assertTrue(form.is_valid())
