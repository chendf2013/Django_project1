from django.conf.urls import url

from viewset import views


# 使用routers实现快速路由分发
from rest_framework import routers
from viewset.views import BookInfoViewSet

# 一、实例化路由对象
router = routers.SimpleRouter()
# 注册路由信息（做三件事）

# 二、一个router可以注册多个视图集(1、当需要单数形式时（detail=True），
# 会自动补充形参正则表达式)\2、还会自动将自定义的动作拼接到路径中，
# 3、使用base_name以基准，将路由的名字变为book-list,book-update等
router.register(r"books",BookInfoViewSet,base_name="book")

urlpatterns = [

]
# 四、将形成的路由追加到urlpatterns中
urlpatterns += router.urls

# urlpatterns = [
#     # url(r"^books/$", views.BaseBookInfoViewSet.as_view({"get": "list","post": "create"})),
#     # url(r"^books/$", views.BaseBookInfoViewSet.as_view({"post": "create"})),(一个路径对应所有的请求方式)
#     # url(r"^books/(?P<pk>\d+)/$", views.BaseBookInfoViewSet.as_view({"get": "retrieve","delete": "destroy","put": "update"})),
#
#     url(r"^books/$", views.UserBookInfoViewSet.as_view({"get": "list", "post": "create"})),
#     url(r"^books/(?P<pk>\d+)/$",views.UserBookInfoViewSet.as_view({"get": "retrieve",
#                                            "delete": "destroy", "put": "update"})),
#
#     # url(r"^books/$",views.BookInfoViewSet.as_view({"get":"latest"})),
#     # url(r"^books/(?P<pk>\d+)/$",views.BookInfoViewSet.as_view({"put":"override_read"})),
# ]
