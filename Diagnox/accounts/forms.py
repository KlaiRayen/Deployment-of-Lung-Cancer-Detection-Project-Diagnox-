# forms.py
from django import forms
from .models import Profile
from django.contrib.auth import authenticate

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['email', 'first_name', 'last_name', 'role', 'password', 'confirm_password', 'img']


class SignInForm(forms.ModelForm):
    password = forms.CharField(
        max_length=100, 
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = "Email"
        self.fields['email'].widget.attrs.update({'style': 'width: 300px;'})

    def clean(self):
        password = self.cleaned_data['password']

        email = self.cleaned_data['email']

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                self.add_error('email', "Email ou mot de passe incorrect.")
                self.add_error('password', "Email ou mot de passe incorrect.")

    class Meta:
        model = Profile
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }
