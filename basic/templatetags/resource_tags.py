from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.tag
def css_link(href, autoescape=None):
  """ Create a helper method to generate links tags for stylesheets. """
  if autoescape:
    esc = conditional_escape
  else:
    esc = lambda x: x
    
  return '<link rel="stylesheet" type="text/css" href="/static/css%s" />' % esc(href)
  
@register.tag
def js_script(src, autoescape=None):
  """ Create a helper method to generate script tags for javascripts. """
  if autoescape:
    esc = conditional_escape
  else:
    esc = lambda x: x
    
  return '<script type="text/javascript" src="/static/js%s"></script>' % esc(src)
  
@register.tag
def img_tag(src, autoescape=None):
  """ Create a helper method to generate img tags for images. """
  if autoescape:
    esc = conditional_escape
  else:
    esc = lambda x: x
    
  return '<img src="/static/images%s"></img>' % esc(src)

