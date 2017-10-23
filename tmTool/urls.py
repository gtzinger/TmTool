from django.conf.urls import patterns, url

import views
from django.contrib import admin

urlpatterns = patterns('',
  url(r'^admin/', admin.site.urls),
  
url(r'^$', views.activity_list, name='activity_list'),
  url(r'^new$', views.activity_create, name='activity_new'),
  url(r'^delete/(?P<pk>\d+)$', views.ActivityDelete.as_view(), name='activity_delete'),
  )