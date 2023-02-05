from django.forms import ModelForm
from .models import Profile

class APIForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['ck_api', 'ck_secret']