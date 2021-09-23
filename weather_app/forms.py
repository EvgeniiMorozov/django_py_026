import re
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from models import CityWeather


class CityForm(ModelForm):

    class Meta:
        model = CityWeather
        fields = ['name']
        widgets = {

        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if not re.match(r"[a-z]", name, flags=re.IGNORECASE):
            raise ValidationError('Название города должно быть на английском!')
        return name
