from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^bar/$', views.ChartView.as_view(), name='bar'),
    url(r'^aar/$', views.AARView.as_view(), name='aar'),
    url(r'^car/$', views.CARView.as_view(), name='car'),
    url(r'^$', views.IndexView.as_view(), name='demo'),
]