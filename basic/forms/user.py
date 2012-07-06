from django import forms

class UserForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField()