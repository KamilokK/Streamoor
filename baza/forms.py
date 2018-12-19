from django import forms
from django.forms import ModelForm

from .models import *

STREAM_TYPE = (
    (1, "Netflix"),
    (2, "HboGo"),
    (3, "Amazon Prime"),
)

class LoginForm(forms.Form):
    user = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)


class AddUserForm(forms.Form):
    user = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(widget=forms.EmailInput)
    user_stream = forms.ChoiceField(choices=STREAM_TYPE)

    def clean(self):

        cleaned_data = super().clean()

        field1 = cleaned_data.get('password')

        user = cleaned_data.get('name')
        if StreamoorUser.objects.filter(user=user).exists():
            self.add_error("user", "Ten użytkownik już jest w bazie!")

        return cleaned_data

