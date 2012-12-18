"""
Views for a Model Compute Request. These requests are made by the user, and then the requests are
processed in a FIFO format. The queue will be executed in an asynchronous manner, thus these
requests will not be processed immediately.
"""

from delayed_jobs import add_delayed_job
from django import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from turbidity.forms.compute_request_form import ComputeRequestForm
from datetime import datetime

ROOT_REQUEST_DIRECTORY = 'request_data'

def create(request, id):
  """
  Create a new request to compute the model.

  GET: Return a page that will allow the user to create a new request.
  POST: Process the information passed in from the create form.
  """
  if request.method != 'GET':
    return render_to_response('compute_request/new.html')

  form = ComputeRequestForm(request.POST, request.FILES)
  if form.is_valid():
    file = request.FILES['file']
    name = file.name
    type = name.split('.').pop() # Split the and then take the last piece.
    user = request.user
    title = form.cleaned_data['title']
    description = form.cleaned_data['description']

    # After the data file has been uploaded and saved, save the request info to the database.
    compute_request = ComputeRequest()
    compute_request.request_by = user
    compute_request.time_requested = datetime.now()
    compute_request.file_type = type
    compute_request.title = title
    compute_request.description = description
    compute_request.save()

    # Generate a hash for the filename to ensure unique filenames for request. Base the has on the
    # id of the compute request.
    compute_request.write_file(file)

    # Add the job to the queue for processing.
    add_delayed_job(__run_request__, compute_request)

  return render_to_response('compute_request/index.html')

def delete(request, id):
  """
  Delete the given compute request. If the request is in the queue, remove it. If it is in process,
  end the processing, and remove it from the queue. After stopping any running processes, ensure
  that the request has been removed from the database and the file system.
  """
  if request.method != 'POST':
    return render_to_response('error_404.html')

  return render_to_response('compute_request/index.html')

def edit(request, id):
  """
  Return a page that will allow the user to modify certain information about the compute request,
  such as the title, description or the priority of the request.

  NOTE: The priority can only be changed by an admin.
  """
  if request.method != 'GET':
    return render_to_response('error_404.html')

  return render_to_response('compute_request/edit.html')

def index(request):
  """
  Return a page with all of the different compute requests that this user is allowed to see.
  """
  if request.method != 'GET':
    return render_to_response('error_404.html')

  return render_to_response('compute_request/index.html')

def show(request, id):
  """
  Show the status and detailed information of a single compute request. This will not contain the
  results of the request, but will have a link to the results page if it is complete.
  """
  if request.method != 'GET':
    return render_to_response('error_404.html')

  return render_to_response('compute_request/show.html')

def update(request, id):
  """
  Modify a compute request, such as the title, description and/or the priority of the request. The
  priority can only be changed by an admin.
  """
  if request.method != 'POST':
    return render_to_response('error_404.html')

  return render_to_response('compute_request/show.html')

# private

def __run_request__(data):
  """
  This method should be called by the delayed jobs processor. That will allow for this request
  to begin processing after previously ran requests are completed. By using a Queue based request
  processing system, employing a highly-fair system, over performance driven.
  """
  # Parse the data provided by the user. The parsing will be determined from the mime-type.
  # Pass the data to the appropriate model for processing.
  print("This is where the model processing should be called")

