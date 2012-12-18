from django.conf.urls.defaults import *

def rest_generator(pkg, resource):
  return patterns(pkg + '.views.' + resource, 
    (r'^$','index'),
    (r'^new/$', 'create'),
    (r'^([0-9]+)/$', 'show'),
    (r'^([0-9]+)/edit/$', 'edit'),
    (r'^([0-9]+)/update/$', 'update'),
    (r'^([0-9]+)/delete/$', 'delete'),
  )

urlpatterns = patterns('',
  (r'^$', 'basic.views.index.index'),
  (r'^personal/$', include(rest_generator('basic', 'personal'))),
  (r'^user/', include(rest_generator('basic', 'user_admin'))),
  (r'^user/login/$', 'basic.views.user_admin.login'),
  (r'^user/logout/$', 'basic.views.user_admin.logout'),
  (r'^compute/$', 'turbidity.views.index.index'),
  (r'^compute_request/', include(rest_generator('turbidity', 'compute_request'))),
  (r'^compute_response/', include(rest_generator('turbidity', 'compute_response'))),
  (r'^admin/', include('admin.urls')),
)
