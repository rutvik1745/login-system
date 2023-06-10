from django import forms
from django.contrib.auth.forms import   PasswordChangeForm, PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Profile


class MyPasswordChangeForm(PasswordChangeForm):
  old_password =forms.CharField(label=_("Old Password"),
  strip=False, widget=forms.PasswordInput(attrs=
  {'autocomplete': 'new-password', 'class':'form-control'}))
  new_password1 = forms.CharField(label=_("New password"),
  strip=False, widget=forms.PasswordInput(attrs=
  {'autocomplete':'new-password','class':'form-control'}),
  help_text=password_validation.
  password_validators_help_text_html())
  new_password2 = forms.CharField(label=_("Confirm New Password"),strip=False, widget=forms.PasswordInput(attrs=
  {'autocomplete':'new-password','class':'form-control'}))

 
class CustmoerProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['name', 'address','city','state','zipcode']
    widgets = {'name':forms.TextInput(attrs=
    {'class':'form-control'}),'address':forms.TextInput(attrs=
    {'class':'form-control'}),'city':forms.TextInput(attrs=
    {'class':'form-control'}),
    'state':forms.Select(attrs={'class':'form-control'}),
    'zipcode':forms.NumberInput(attrs={'class':'form-control'})}


class MyPasswordResetForm(PasswordResetForm):
  email = forms.EmailField(label=_("Email"),max_length=254,
  widget=forms.EmailInput(attrs={'autocomplete':'email',
  'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
  new_password1 = forms.CharField(label=_("New password"),
  strip=False, widget=forms.PasswordInput(attrs=
  {'autocomplete':'new-password','class':'form-control'}),
  help_text=password_validation.
  password_validators_help_text_html())
  new_password2 = forms.CharField(label=_("Confirm New Password"),strip=False, widget=forms.PasswordInput(attrs=
  {'autocomplete':'new-password','class':'form-control'}))
  
