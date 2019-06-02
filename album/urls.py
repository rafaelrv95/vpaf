from django.conf.urls import url, include
from album.views import index

urlpatterns = [
    url(r'^$', index),
]
