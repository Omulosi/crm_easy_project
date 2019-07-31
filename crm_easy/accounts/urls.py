from django.conf.urls import url
from . import views


app_name = 'accounts'
urlpatterns = [
    url(r'^account/list/$', views.AccountList.as_view(), name='account_list'),
]

