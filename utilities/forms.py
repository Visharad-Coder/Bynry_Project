# myapp/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from .models import ServiceRequest


class CustomUserCreationForm(UserCreationForm):
    bio = forms.CharField(max_length=500, required=False)
    email = forms.EmailField(required=False)
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'bio', 'phone_number', 'address']


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['type', 'details', 'files']



