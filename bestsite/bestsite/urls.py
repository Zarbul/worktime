"""bestsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from hardwork import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^detail/$', views.worker_detail),
    url(r'^detail/(?P<id>\d+)/edit/$', views.edit, name='edit'),
    url(r'^detail/(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^new/$', views.new, name='new'),
    # url(r'^save+', views.save),
    # url(r'^delete/(?P<id>\d+)/$', views.delete),
    url(r'^$', views.home),
]