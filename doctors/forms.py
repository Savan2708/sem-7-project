from django import forms
from django.forms import ModelForm
from userprofile.models import UserProfile


class BookForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
