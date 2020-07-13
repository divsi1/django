from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url('res/',views.resAll,name="res"),
    url('postURL/',views.createpostURL,name="addurls"),
]
