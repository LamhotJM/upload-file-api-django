from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from commentengine import views
from commentengine.views import schema_view

urlpatterns = patterns('',
                       url(r'comments/$', views.MasterCommentList.as_view()),
                       url(r'^comments/(?P<pk>[0-9]+)/$', views.MasterCommentDetail.as_view()),
                       url('/', schema_view)
                       )
