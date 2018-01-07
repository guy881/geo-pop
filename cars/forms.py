import datetime
import re

from django import forms
from django.forms import ModelForm

from .models import Car


class CarForm(ModelForm):
    class Meta:
        model = Car
        exclude = ['last_location']

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean(self):
        cleaned_data = super(CarForm, self).clean()

        brand = cleaned_data.get('brand')
        model = cleaned_data.get('model')
        production_year = cleaned_data.get('production_year')
        engine_volume = cleaned_data.get('engine_volume')
        body_type = cleaned_data.get('body_type')
        need_repair = cleaned_data.get('need_repair')
        insurance_number = cleaned_data.get('insurance_number')
        is_available = cleaned_data.get('is_available')

        if not self.instance.pk and Car.objects.filter(insurance_number=insurance_number).exists():
            self.add_error('insurance_number', forms.ValidationError('W bazie istnieje już samochód o podanym numerze ubezpieczenia'))
        if not brand.isalpha():
            self.add_error('brand', forms.ValidationError('Nazwa marki może się składać tylko z liter!'))
        if not re.match("^[A-Za-z0-9_-]+$", model):
            self.add_error('model', forms.ValidationError('Nazwa modelu może się składać tylko z liter i cyfr!'))
        if production_year <= 1769 or production_year > datetime.datetime.now().year:
            self.add_error('production_year', forms.ValidationError('Rocznik poza zakresem!'))
        if engine_volume <= 0.0 or engine_volume >= 10000.0:
            self.add_error('engine_volume', forms.ValidationError('Pojemność silnika poza zakresem!'))
        if insurance_number and not re.match("^[A-Za-z0-9_-]+$", insurance_number):
            self.add_error('insurance_number', forms.ValidationError('Numer ubezpieczenia może się składać tylko z liter i cyfr!'))
        if self._errors:
            self.add_error(None, forms.ValidationError('Uprzejmie proszę o poprawienie błędów :)'))

        return cleaned_data
