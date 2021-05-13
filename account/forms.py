from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Repeat password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs=
                                       {'class': 'form-control',
                                        'placeholder': 'User name'}),
            'first_name': forms.TextInput(attrs=
                                       {'class': 'form-control',
                                        'placeholder': 'First name'}),
            'email': forms.TextInput(attrs=
                                       {'class': 'form-control',
                                        'placeholder': 'Email address'}),
            }

        labels = {
            'username': 'User name',
            'first_name': 'First name',
            'email': 'Email address',
            }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs=
                                       {'class': 'form-control',
                                        }),
            'last_name': forms.TextInput(attrs=
                                       {'class': 'form-control',
                                        }),
            'email': forms.TextInput(attrs=
                                       {'class': 'form-control',
                                        }),
            }

        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email address',
            }