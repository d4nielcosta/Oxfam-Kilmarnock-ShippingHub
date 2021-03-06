__author__ = 'daniel'

from django.conf.urls import *

import views

urlpatterns = patterns('',
                       # url(r'^$', views.manager, name='manager'),
                       url(r'^index/$', views.index, name='index'),
                       url(r'^storerank/$', views.storerank, name='storerank'),
                       url(r'^dev/$', views.dev, name='dev'),
                       url(r'^allstores/$', views.allstores, name="allstores"),
                       )
