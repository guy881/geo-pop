from django.forms import ModelForm

from .models import Car

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'production_year','engine_volume','body_type','need_repair','insurance_number','is_available','last_location']
