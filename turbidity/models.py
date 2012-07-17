from django.db import models
from parsers import RequestParser
from parsers import ResponseParser
from django.contrib.auth.models import User

class ComputeRequest(models.Model):
  """
  The request itself will be in a file associated with the id of this request. The data will be
  stored in a YAML format, which will allow it to be human readable, as well as utilize many
  mechanisms that already can write in that format.
  """

  # A description of this run, and what it is for.
  description = models.CharField(blank=True)
  # The type of the file that was uploaded. e.g. csv, txt
  file_type = models.CharField()
  # The user that was logged in and requested for the job to be done.
  request_by = User()
  # The time that the job was requested to be done.
  time_requested = models.DateTimeField()
  # The title of this request (Optional)
  title = models.CharField(blank=True)

  def request_data(self, request_parser=None):
    """ Retrieve the data that is associated with this request. """
    if self.id == None:
      return {}

    path = self.__get_path__()
    lines = []
    with open(path, 'r') as f:
      lines = f.readlines()

    if request_parser == None:
      data = request_parser.parse(lines)
    else:
      data = lines

    return output

  def write_file(self, request_file):
    """
    Take the file passed in from the web request, and write out the contents to the file specified.
    If the filename is blank, or the request file is empty, an exception will be thrown as this is
    a serious problem, and should be addressed immediately.
    """
    if request_file is None:
      raise Exception('The provided file is null.')

    with open(self.__get_path__(), 'w') as request_fh:
      for chunk in request_file.chunks():
        request_fh.write(chunk)

  # private

  def __get_path__(self):
    """ Get the path of the data associated with this request. """
    return os.path.abspath('request_data/req_' + self.id + '.data')

class ComputeResponse(models.Model):
  """
  The response data will be in a file associated with the id of this response. The storage format
  will be the same as the compute request resources.
  """

  time_completed = models.DateTimeField()
  request = ComputeRequest()

  def response_data(self, response_parser=None):
    """ Retrieve the data that is associated with this response. """
    if self.id == None:
      return {}

    path = os.path.abspath("response_data/resp_" + self.id + ".yml")
    with open(path, 'r') as f:
      lines = f.readlines()

    if response_parser == None:
      data = response_parser.parse(lines)
    else:
      data = lines

    return output

