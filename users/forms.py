from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'password1',
            'password2',
            'full_name',
            'personal_number',
            'birth_date',
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        try:
            validate_password(password)
        except ValidationError as e:
            raise forms.ValidationError(e.messages)
        return password

    def clean_personal_number(self):
        personal_number = self.cleaned_data.get('personal_number')
        if not personal_number.isdigit():
            raise forms.ValidationError('Personal number must be numeric.')
        return personal_number