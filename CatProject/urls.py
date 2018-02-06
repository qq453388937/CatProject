# coding=utf-8
"""CatProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin

# import booktest.views   ==> url(r"^$", booktest.views.index)
# from booktest.views import *  ==> url(r"^$",index)
# from booktest import views  # ==> url(r"^$", views.index)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r"^OA/", include("OA.uls", namespace="OAmain")),
    # url(r"^", include("booktest.urls"))  # include need r"^" __init__

    url(r"^booktest/", include("booktest.urls", namespace="main")),  # namespace ??
    # tinymce 添加路径
    url(r'^tinymce/', include('tinymce.urls')),
    # haystack 添加路径
    url(r'^search/', include('haystack.urls')),

    url(r'^oa/', include('OA.urls', namespace='oa'))
]
