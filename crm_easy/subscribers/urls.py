from django.conf.urls import url
from . import views

app_name = 'subscribers'
urlpatterns = [
    url(r'^signup/$', views.subscriber_new, name='sub_new')
]
