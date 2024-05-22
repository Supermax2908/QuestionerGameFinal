from django import forms
from .models import Test

class CreateTestForm(forms.ModelForm):
    class Meta:
        model=Test
        fields = ('topic', 'description')