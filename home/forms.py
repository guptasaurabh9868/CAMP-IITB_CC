from django import forms
from .models import UserProfile

class PasswordChangeForm(forms.ModelForm):
    model = UserProfile
    fields = ('userPassword','first_name')