# coding=utf-8
from haystack import indexes  # 引入haystack
from models import * # 引入models类

# 类名可以自定义
class BookInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return BookInfo

    def index_queryset(self, using=None):
        return self.get_model().books1.all()


class HeroInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return HeroInfo

    def index_queryset(self, using=None):
        return self.get_model().objects.all() # 对哪些数据进行检索可以限制范围
