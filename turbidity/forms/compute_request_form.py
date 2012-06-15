from django import forms

class ComputeRequestForm(forms.Form):
  """
  
  """
  time_requested = forms.DateField()
  priority = forms.IntegerField()
  requestor = forms.CharField()
