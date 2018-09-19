
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^bookview/$', views.Bookview.as_view()),
    url(r'^index/$', views.index),
    ]
