from django import forms
from .models import Short


class ShortForm(forms.ModelForm):
    bookmark = forms.CharField(widget=forms.TextInput, label='')

    class Meta:
        model = Short
        fields = ('bookmark',)
