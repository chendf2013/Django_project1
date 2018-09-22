
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^", include("booktest.urls")),
    url(r"^", include("apiview.urls")),
    url(r"^",include("viewset.urls")),

]
