from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email","password1","password2",)

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"


class FileForm(forms.Form):
    file_upload = forms.FileField()
    key = forms.FileField()

