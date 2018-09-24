from django.conf.urls import url

from . import views

urlpatterns=[
    url(r"^user/$",views.user_cookie),
    url(r"user2/$",views.user_cookie_read),
]