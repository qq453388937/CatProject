# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^test/$', test),
    url(r'^booklist/$', bookList),
    url(r'^(\d+)/$', peopleList),

]
