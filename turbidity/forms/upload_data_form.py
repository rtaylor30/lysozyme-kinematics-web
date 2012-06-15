from django import forms

class UploadDataForm(forms.Form):
  """
  
  """
  filename = forms.CharField()
  file = forms.FileField()
  request_id = forms.IntegerField()
