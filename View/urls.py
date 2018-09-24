from django.conf.urls import url
from . import views

# as_view()方法将类视图转化为函数，供django调用使用
urlpatterns = [
    url(r"^view/$",views.ViewP.as_view())

]