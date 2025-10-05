from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_image", "bio"]  # ✅ match the model fields
