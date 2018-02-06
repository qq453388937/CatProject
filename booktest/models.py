# coding=utf-8
from django.db import models
from tinymce.models import HTMLField


# 重写管理器默认查询功能  ==>  BookInfo 类里指向该管理器所以是BookInfo表
class BookInfoManager(models.Manager):  # => 管理器集成自 models.Manager
    """自定义管理器 = 》 更改默认查询集"""

    # 自定义查询集合
    def get_queryset(self):
        """更改默认查询集"""
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)

    # 自定义新增查询集的方法 通过管理器
    # django官方推荐初始化快捷方法,不能重写BookInfo的__init__方法，通过BookInfo.books2.create("....")

    def create(self, btitle, bpubdate):
        """第二种在管理器中自定义初始化模型类  django推荐使用第二种
            BookInfo.object.create() 类对象调用也可以
            BookInfo().create() 对象调用也可以
        """
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpubdate
        b.bread = 0
        b.bcomment = 0
        b.isDelete = False
        return b  # 将创建好的对象返回最后save()


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name="书名")
    bpub_date = models.DateTimeField(db_column="pub_date")
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0, null=False)  # null=True可以为空 null=False不能为空

    isDelete = models.BooleanField(default=0)  # NullBooleanField
    pic = models.ImageField(upload_to="upload/", default=None)

    # 自定义管理器 至少一个！
    # 默认的objects=Manager() 会被重写  原来django的objects管理器就会失效！
    # 使用自定义管理器对象 在model中重写
    books1 = models.Manager()  # 仅仅是重命名 没有太大意义
    books2 = BookInfoManager()  # 管理器对象作为模型类的属性去才能知道是对应哪个表　,元选项中有表名db_table

    # python  层面的应用 不推荐
    @classmethod
    def quick_create(cls, btitle, bpubdate):
        """自定义初始化模型类的方法不能重写__init__方法"""
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpubdate
        b.bread = 0
        b.bcomment = 0
        b.isDelete = False
        return b  # 将创建好的对象返回最后save()

    def __str__(self):
        # return self.btitle+str(self.bpub_date)
        return u"BookInfo该对象属性的值是[btitle:%s] [bpub_date:%s]" % (
            self.btitle, str(self.bpub_date)
        )
        # return "BookInfo该对象属性的值是[btitle:%s] [bpub_date:%s]" % (
        #     self.btitle.encode("utf-8"), str(self.bpub_date).encode("utf-8")
        # )

    def show_name(self):
        return self.btitle
        # 元选项

    class Meta:
        # 更改原来数据中默认的table的名字！
        db_table = "bookinfo"
        # ordering = ["id"]


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000, null=True)

    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo)  # 外键引用对象 mysql 查看得到book_id 外键字段   加引号可以不规定限制BookInfo类的定义顺序

    # book = models.ForeignKey("BookInfo")
    # 用于admin显示自定义字符串
    def nice_gender(self):
        if self.hgender:
            return '男'
        else:
            return '女'

    # 用于admin显示自定义字段
    nice_gender.short_description = "性别"

    def __str__(self):
        # return self.hname+self.hcontent
        return "英雄名称：%s 英雄性别　%s 内容 %s" % (
            self.hname.encode("utf-8"), str(self.hgender).encode('utf-8'), self.hcontent.encode("utf-8")
        )

    # 问题编码
    class Meta:
        db_table = "heroInfo"
        ordering = ["id"]


class Area(models.Model):
    atitle = models.CharField(max_length=20)
    aPid = models.ForeignKey("self", null=True, blank=True, db_column="pid")

    class Meta:
        db_table = "areas"


class AreaInfo(models.Model):
    areaTitle = models.CharField(max_length=20)
    areaPid = models.ForeignKey("self", null=True, blank=True, db_column="pid")

    class Meta:
        db_table = "areainfo"


class TinyMce(models.Model):
    comment = HTMLField()

    class Meta:
        db_table = "tinymce"


# 上传图片的模型
class PictureInfo(models.Model):
    """
    # 上传图片路径  (booktest 在模型中upload to 中指定！！！！灵活性)
    MEDIR_ROOT = os.path.join(BASE_DIR, "static/upload/")
    """
    # upload_to：表示图片上传到哪儿 ,setings.py中已经定义好根基上传目录
    path = models.ImageField(upload_to='booktest/')

    # 元类信息 ：修改表名
    class Meta:
        db_table = 'pictureinfo'
