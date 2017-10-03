from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_page),
    url(r'^callback', views.callback),
]
