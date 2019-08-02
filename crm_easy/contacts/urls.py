from django.conf.urls import url
from . import  views


app_name = 'contacts'
urlpatterns = [
    url(r'^contact/(?P<uuid>[\w-]+)/$', views.contact_detail,
        name='contact_detail'),
]
