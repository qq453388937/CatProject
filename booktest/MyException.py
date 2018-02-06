# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import logging


# 任意一个自定义的ｐｙ文件任意的自定义类重写５个方法即可
class MyException():
    @staticmethod
    def myfile(msg):
        """输出到文件(追加方式)"""
        logging.basicConfig(level=logging.DEBUG,
                            filename='./logger.txt',
                            filemode='a',
                            format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        logging.error(msg)



    def process_exception(request, response, exception):
        MyException.myfile(exception.message)
        return HttpResponse(exception.message)
