from django.forms import ModelForm
from .models import API

class APIForm(ModelForm):
    class Meta:
        model = API
        fields = '__all__'