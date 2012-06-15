
# ======== Parser ==================================================================================

class Parser():
  """
  Root parser class, that is meant to enfore the implementation of the method __parse, and abstract
  away some common functionality between the different parsers.
  
  This parser is designed to parse information from the stored YAML data. The storage format for
  YAML is for primitives, and the actual parsing into a usable data structure is done through here.
  """
  
  def __init__(self, data=None):
    """ If the data is provided upon instantiation, will run the parser immediately. """
    if data != None:
      self.parse(data)
  
  def parse(self, data):
    """ The public method to run the parser. If no data is provided, an exception is thrown """
    if data == None:
      raise ParseException()
      
    self.__parse(data)
  
  def __parse(self, data):
    """ Method to be implemented by a subclass. """
    raise NotImplementedException()

# ======== RequestParser ===========================================================================

class RequestParser(Parser):
  """ A parser implementation for the compute request data. """
  
  def __init__(self, data=None):
    super(RequestParser, self).__init__(data)

# ======== ResponseParser ===========================================================================    
    
class ResponseParser(Parser):
  """ A parser implementation for the compute response data. """
  
  def __init__(self, data=None):
    super(ResponseParser, self).__init__(data)

# ==================================================================================================
# Exception Classes
# ==================================================================================================
    
class ParseException(Exception):
  pass

class NotImplementedException(Exception):
  pass
  