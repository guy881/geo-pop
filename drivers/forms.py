from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
import re
from . import models
from cars import models as models_c
from django.forms.models import inlineformset_factory
from django.forms import ImageField


class DriverBasicForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', False)
        super().__init__(*args, **kwargs)
        # self.fields['pesel'].widget.attrs['disabled's] = True

    class Meta:
        model = models.Driver
        fields = ('full_name', 'gender', 'pesel', 'phone_number')

    def pesel_check(self, pesel):
        if (re.match('[0-9]{11}$', pesel)):
            pass
        else:
            return 0
        l = int(pesel[10])
        suma = ((l * int(pesel[0])) + (3 * int(pesel[l])) + (7 * int(pesel[2])) + (9 * int(pesel[3])) + (
        (l * int(pesel[4]))) + (3 * int(pesel[5])) + (7 * int(pesel[6])) + (9 * int(pesel[7])) + (l * int(pesel[8])) + (
                3 * int(pesel[9])))
        controlbit = 10 - (suma % 10)
        if controlbit == 10:
            controlbit = 0
        else:
            controlbit = controlbit

        if ((controlbit == 10) or (controlbit == 0)):
            return 0
        else:
            return 1

    def clean(self):
        cleaned_data = super().clean()
        full_name = cleaned_data.get("full_name")
        phone_number = cleaned_data.get("phone_number")
        gender = cleaned_data.get("gender")
        pesel = cleaned_data.get("pesel")

        if full_name and  not ' ' in full_name:
                    self.add_error('full_name', ValidationError('Give full name'))

        if phone_number:
            reg = '(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{3}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{3}|\d{3}[-\.\s]??\d{3}|\d{9})$'
            pattern = re.compile(reg)
            if not  pattern.match(phone_number):
                self.add_error('phone_number', ValidationError('Phone number is in bad format'))

        if gender:
            reg = '(m|f|k|apache helicopter|man|female|male|women|kobieta|mężczyzna|other|inne)$'
            pattern = re.compile(reg.rstrip())
            if not pattern.match(gender.lower()):
                self.add_error('gender', ValidationError('Gender is in bad format'))

        if pesel and not self.pesel_check(pesel):
            self.add_error('pesel', ValidationError('Pesel is in bad format'))

        return cleaned_data


class DriverImageForm(forms.ModelForm):
    image = ImageField(
        required=False
    )

    class Meta:
        model = models.Driver
        fields = ('image',)
        # exclude = ('full_name', 'gender', 'pesel', 'phone_number')

    def __init__(self, *args, validate=True, **kwargs):
        super().__init__(*args, **kwargs)
        self.validate = validate

    def clean(self):
        cleaned_data = super().clean()
        empty_fields_set = set([field for field, val in cleaned_data.items() if not val])
        if self.validate:
            for field in empty_fields_set:
                self.add_error(field, ValidationError(_('This field is required!')))
        return cleaned_data



class DriverCarsForm(forms.ModelForm):
    class Meta:
        model = models.Driver
        fields = ()

    def clean(self):
        cleaned_data = super().clean()
        empty_fields_set = set([field for field, val in cleaned_data.items() if not val])

        for field in empty_fields_set:
            self.add_error(field, ValidationError(_('This field is required!')))
        return cleaned_data


# CarFormSet_no_extra = inlineformset_factory(models_c.Car, models.Driver, fields=('is_available', 'state', 'coordinates', 'velocity'), extra=0)
# CarFormSet = inlineformset_factory(models_c.Car, models.Driver, fields=('is_available', 'state', 'coordinates', 'velocity'), extra=1)


