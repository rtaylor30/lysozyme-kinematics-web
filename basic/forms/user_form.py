from django import forms

class UserForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField()

class AuthorizationForm(forms.Form):
  """
  Form used to authorize a user when they are logging in.
  """
  username = forms.CharField()
  password = forms.CharField()
