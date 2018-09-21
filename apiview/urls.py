
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api.books/$', views.BookDetailView.as_view()),
    # url(r'^api.books/(?P<pk>\d+)/$', views.BookDetailAPIView.as_view()),
    url(r'^api.books/$', views.BookListAPIView.as_view()),
    url(r'^api.books/(?P<pk>\d+)/$', views.BookdetailAPIView.as_view()),

]
