from django import forms
from .models import PlatformUser


class UserForm(forms.ModelForm):
    class Meta:
        model = PlatformUser
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'card_id': 'ID',
            'username': 'Username',
            'password': 'Password'
        }
        widgets = {
            'password': forms.PasswordInput()
        }
