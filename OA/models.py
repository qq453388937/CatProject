# -*- coding:utf-8 -*-
from django.db import models


# Create your models here.

class BookInfo(models.Model):
    """书籍信息"""
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name.encode()

    class Meta:
        db_table = "OA_BookInfo"


class PeopleInfo(models.Model):
    """人物信息模型类"""
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "OA_PeopleInfo"
