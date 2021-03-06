"""crmapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from crm_easy.marketing.views import HomePage

urlpatterns = [
    # Marketing pages
    url(r'^$', HomePage.as_view(), name="home"),

    # Subscriber related URLs
    url(r'',
        include('crm_easy.subscribers.urls')),
    # Admin URL
    url(r'^admin/', include(admin.site.urls)),

    # Login/Logout URLs
    url(r'^login/$', LoginView.as_view(template_name='login.html'),
        name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    # Account related URLs
    url(r'', include('crm_easy.accounts.urls')),

    # Contact related URLs
    url(r'', include('crm_easy.contacts.urls')),

    # Communication related URLs
]

