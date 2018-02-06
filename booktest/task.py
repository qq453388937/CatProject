# -*- coding:utf-8 -*-
import time

from celery import task
from django.http import  *


@task
def show():
    print("hello1")
    time.sleep(5)
    print("hello2")
    return 1

# sayhello.delay()
    #return HttpResponse("hello world over")