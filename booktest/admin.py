# coding:utf-8
from django.contrib import admin
# 1
# from booktest.models import *
# 2  python2
# from models import *
# 3  python3
from .models import *


# Register your models here.
# 此类必须在BookInfoAdmin之前申明否则访问不到  inlines = [HeroInfoInline]
# 关联注册的前提是定义关联注册类和关联的对象以及个数  最后在自定义关联对象的inlines=[]数组中添加该关联注册的对象
class HeroInfoInline(admin.StackedInline):
    model = HeroInfo  # 嵌入哪个类 嵌入的类必须有该外键！
    extra = 2


class BookInfoAdmin(admin.ModelAdmin):
    # 指定后台站点显示的该表字符串
    list_display = ["id", "btitle", "bpub_date", "bread", "bcomment", "isDelete", "pic"]
    list_filter = ["btitle"]
    search_fields = ["btitle"]
    actions_on_bottom = True
    list_per_page = 20
    # 属性分组  增加页面和修改页面
    fieldsets = [
        ("basic", {"fields": ["btitle"]}),
        ("nomal", {"fields": ["bpub_date", "bread", "bcomment"]})

    ]
    inlines = [HeroInfoInline]


    # 指定方法作为列的排序依据


# 2.第二种方式注册
@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "hname", "nice_gender", "hcontent", "isDelete"]
    list_filter = ["hname"]
    search_fields = ["hname", "hgender"]
    list_per_page = 20
    # 属性分组 增加页面和修改页面
    fieldsets = [
        ("basic", {"fields": ["hname"]}),
        ("more fields", {"fields": ["hgender", "hcontent"]})

    ]


@admin.register(TinyMce)
class TinyMceAdmin(admin.ModelAdmin):
    list_display = ["id", "comment"]
    list_filter = ["comment"]
    search_fields = ["comment"]
    list_per_page = 20


# 1.后台注册模型类(定义好model后就可以注册)和自定义展示列表页和更改页面
admin.site.register(BookInfo, BookInfoAdmin)
# admin.site.register(HeroInfo, HeroInfoAdmin)
