from django.conf.urls import url
from . import views


app_name = 'accounts'
urlpatterns = [
    url(r'^account/new/$', views.account_cru, name='account_new'),
    url(r'^account/list/$', views.AccountList.as_view(), name='account_list'),
    url(r'^account/(?P<uuid>[\w-]+)/$', views.account_detail, name='account_detail'),
]

