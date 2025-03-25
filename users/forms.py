from django import forms
from .models import User_db

class SignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User_db  
        fields = ['name', 'nid', 'phone', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data

    def save(self, commit=True):
        """Save the user with plain text password """
        user = super().save(commit=False)
        user.password = self.cleaned_data["password"]  # ⚠️ Storing plain text password
        if commit:
            user.save()
        return user


# Login Form
class LoginForm(forms.Form):
    nid = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)


