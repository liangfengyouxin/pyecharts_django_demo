from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^bar/$', views.ChartView.as_view(), name='demo'),
    url(r'^$', views.IndexView.as_view(), name='demo'),
]