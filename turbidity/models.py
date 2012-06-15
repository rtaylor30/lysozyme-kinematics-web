from django.db import models
from parsers import RequestParser
from parsers import ResponseParser

class ComputeRequest(models.Model):
  """
  The request itself will be in a file associated with the id of this request. The data will be 
  stored in a YAML format, which will allow it to be human readable, as well as utilize many 
  mechanisms that already can write in that format.
  """
  
  time_requested = models.DateTimeField()
  request_by = models.User()
  
  def request_data(self, request_parser=None):
    """ Retrieve the data that is associated with this request. """
    if self.id == None:
      return {}
    
    path = os.path.abspath("request_data/req_" + self.id + ".yml")
    lines = []
    with open(path, 'r') as f:
      lines = f.readlines()
      
    if request_parser == None:
      data = request_parser.parse(lines)
    else:
      data = lines
      
    return output

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
  