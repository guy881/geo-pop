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
