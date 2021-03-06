from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from buildApp.models import Orders, Feedback


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('Comment', 'Phone')


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('TextFeedback', 'File')
