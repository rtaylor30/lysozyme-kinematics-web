from django import forms

class ComputeRequestForm(forms.Form):
  """
  A request for some work to be done. This request requires a file to work on.
  The processing of the file will be deferred to later, as this job will be added to a processing
  queue.
  """
  description = forms.CharField()
  file = forms.FileField()
  title = forms.CharField()
  
  # TODO : Add a prioritization mechanism.
