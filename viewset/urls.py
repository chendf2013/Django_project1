from django.conf.urls import url

from viewset import views

urlpatterns = [
    # url(r"^books/$", views.BaseBookInfoViewSet.as_view({"get": "list","post": "create"})),
    # url(r"^books/$", views.BaseBookInfoViewSet.as_view({"post": "create"})),(一个路径对应所有的请求方式)
    # url(r"^books/(?P<pk>\d+)/$", views.BaseBookInfoViewSet.as_view({"get": "retrieve","delete": "destroy","put": "update"})),

    url(r"^books/$", views.UserBookInfoViewSet.as_view({"get": "list", "post": "create"})),
    url(r"^books/(?P<pk>\d+)/$",views.UserBookInfoViewSet.as_view({"get": "retrieve",
                                           "delete": "destroy", "put": "update"})),

    # url(r"^books/$",views.BookInfoViewSet.as_view({"get":"latest"})),
    # url(r"^books/(?P<pk>\d+)/$",views.BookInfoViewSet.as_view({"put":"override_read"})),
]
