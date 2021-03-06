from django.conf.urls import url
from . import  views


app_name = 'contacts'
urlpatterns = [
    url(r'^contact/new/$', views.contact_cru, name='contact_new'),
    url(r'^contact/(?P<uuid>[\w-]+)/edit/$', views.contact_cru,
        name='contact_update'),
    url(r'^contact/(?P<uuid>[\w-]+)/$', views.contact_detail,
        name='contact_detail'),

    url(r'^contact/(?P<pk>[\w-]+)/delete/$',
        views.ContactDelete.as_view(), name='contact_delete'),
]
