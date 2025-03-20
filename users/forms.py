from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'nid', 'phone', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data


# Login Form
class LoginForm(forms.Form):
    nid = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
