from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """Authenticate users against the database"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        # if the user chooses a username that already exists, they will get a validation error
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        """
        Custom validation
        you can provide a clean_<fieldname>() method to amy of your form fields in order to clean the value
        or raise form validation errors for a specific field.
        """
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']
