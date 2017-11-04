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
        super().__init__(*args, **kwargs)
        # self.fields['pesel'].widget.attrs['disabled'] = True

    class Meta:
        model = models.Driver
        fields = ('full_name', 'gender', 'pesel', 'phone_number')


    def clean(self):
        cleaned_data = super().clean()
        tmp = [(f,v)for f,v in cleaned_data.items()]
        for field,val in tmp:
            if field=='full_name':
                if not ' ' in val:
                    self.add_error(field, ValidationError('Give full name'))
            elif field == 'phone_number':
                reg = '(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{3}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{3}|\d{3}[-\.\s]??\d{3}|\d{9})$'
                pattern = re.compile(reg)
                if not  pattern.match(val):
                    self.add_error(field, ValidationError('Phone number is in bad format'))
            elif field == 'gender':
                reg = '(m|f|k|apache helicopter|man|female|male|women|kobieta|mężczyzna|other|inne)$'
                pattern = re.compile(reg.rstrip())
                if not pattern.match(val.lower()):
                    self.add_error(field, ValidationError('Gender is in bad format'))
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


CarFormSet_no_extra = inlineformset_factory(models.Driver, models_c.Car, fields=('is_available', 'state', 'coordinates', 'velocity'), extra=0)
CarFormSet = inlineformset_factory(models.Driver, models_c.Car, fields=('is_available', 'state', 'coordinates', 'velocity'), extra=1)


