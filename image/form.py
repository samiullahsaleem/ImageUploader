from django.forms import ModelForm

from .models import image

class imageForm(ModelForm):
    class Meta:
        model = image
        fields = ['image']