from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone

from . import models


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True)
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(max_length=254,required=True)
    gender = forms.ChoiceField(choices=(('M', 'Male'),
                                        ('F', 'Female'),
                                        ('O', 'Other')))
    date_joined = forms.DateField(initial=timezone.now)

    class Meta:
        model = models.CustomUser
        fields = ("username",
                  "avatar",
                  "first_name",
                  "last_name",
                  "email",
                  "gender",
                  "date_joined")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('The email address must be unique')
        return email


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = ('avatar',
                  'bio')
