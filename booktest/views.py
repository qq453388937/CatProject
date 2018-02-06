# coding:utf-8
import os
import random
from django.http import *  # 默认的旧的方式,返回httpresponse 必须引用该模块
# loader 加载模板 render用了无需用这个
from django.template import RequestContext, loader
from django.shortcuts import render, redirect
from .models import *  # 推荐使用
# from models import *
# from  . import  models
# 使用逻辑与逻辑或和QF对象
from django.db.models import *  # Max F ,Q
from datetime import *
from django.core.urlresolvers import reverse  # 反向解析引用
# 如果想用django中配置文件的变量需要导入包
from django.conf import settings
# 分页需要导包
from django.core.paginator import *

# 缓存需要的包
from django.views.decorators.cache import cache_page
# 底层缓存需要导入的包
from django.core.cache import cache
# celery 需要引入的包
from task import *
# 百度解决post csrf 问题
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# Max
def test(request):
    return HttpResponse("ok")


def index(request):  # 必须
    book_list = BookInfo.books1.filter(heroinfo__hcontent__contains="八")
    # maxdate=book_list.aggregate(Max("bpub_date"))
    read_count_list = BookInfo.books1.filter(bread__gt=10)
    # F对象
    read_count_more_pinglun_list = BookInfo.books1.filter(bread__gt=F("bcomment"))
    # filter 后最后聚合aggregate
    maxbread = BookInfo.books1.aggregate(Max("bread"))
    q_model_list = BookInfo.books1.filter(Q(pk__gt=2) | Q(bcomment__gt=10))
    not_q_model = BookInfo.books1.filter(~Q(pk__gte=3))
    # 关联查询1                            没有外键的使用关联类名消协
    inner_join_1 = BookInfo.books1.filter(heroinfo__hcontent__contains="葵花")
    # 关联查询2                             有外键的优先使用外键替换关联类名小写
    inner_join_2 = HeroInfo.objects.filter(book__btitle__contains="天")

    context = {
        "book_list": book_list,
        "read_count_list": read_count_list,
        "maxbread": maxbread,
        "read_count_more_pinglun_list": read_count_more_pinglun_list,
        "q_model_list": q_model_list,
        "not_q_model": not_q_model,
        "inner_join_1": inner_join_1,
        "inner_join_2": inner_join_2
    }
    # return need request first
    # settings.py里配置了模板搜索文件夹的路径但是这里还需要指明是哪个模块的，可能有多个模块
    return render(request, "booktest/index.html", context)


"""关联创建"""


# h=b.heroinfo_set.create(htitle=u'黄蓉',hgender=False,hcontent=u'打狗棍法')

# showdetail 反向先配路由再定义方法，最后定义页面html
# html页面如果需要传递参数 ，可以通过正则分组传参lllllllllllllllllllllllll
def show_new_detail(request, id):
    # return HttpResponse("testid:%s" % id) # 简单测试

    bookone = BookInfo.books1.get(pk=id)
    #  关联查询
    herolist = bookone.heroinfo_set.all()
    # 不能直接heroinfo_set() 调用.all方法否则会 'RelatedManager' object is not iterable
    context = {"bookone": bookone, "id": id, "herolist": herolist}
    return render(request, "booktest/newdetail.html", context)


def show_new_detail2(request, id):
    # 只查询出书不查询英雄的方式
    bookone = BookInfo.books1.get(pk=id)
    context = {"bookone": bookone}

    return render(request, "booktest/newdatail2.html", context)


def old_response(request):
    return HttpResponse("hello word_response")


def printf_ids(request, id):
    return HttpResponse(id)


# 不给组起别名的情况 =》位置参数  接受过来的参数都是字符串
def print_ids(request, p1, p2, p3):
    context = "%s/%s/%s" % (p1, p2, p3)
    return HttpResponse(context)


# 给正则分组起名 =》命名参数（和组名一致）  分组后接受过来的参数都是字符串
def print_group_ids(request, myid, secondid, thirdid):
    return HttpResponse("%s/%s/%s" % (myid, secondid, thirdid))


def new_style(request):
    # 默认传递context的格式是字典
    booklist = BookInfo.books1.all()
    context = {"testdata": "测试新式写法数据data", "booklist": booklist}
    # return request()
    return render(request, "booktest/newstyle.html", context)


def select(request):
    """语法：属性名称__比较运算符"""
    # bookinfo_qiepian = BookInfo.books1.all()[0:2]
    bookinfo = BookInfo.books1.filter(btitle__contains="%").first()  # 匹配%不用转义直接写%
    book_exclude = BookInfo.books1.exclude(pk=3)
    # bookinfo = BookInfo.books1.exclude(btitle__contains="%").last() # 和filter相反不包含%的
    bookinfo_model = BookInfo.books1.get(id=1)
    # filter 方法btitle__iendswith等  i  字母开头的是不去分大小写的
    bookinfo_exist = BookInfo.books1.filter(btitle__contains="编程").exists()
    # 以。。。。结尾 | 开头   BookInfo.books1.filter(btitle__startswith="....")
    bookinfo_endwith_model = BookInfo.books1.filter(btitle__endswith="嘿").first()
    bookinfo_isnotnull_count = BookInfo.books1.filter(btitle__isnull=False).count()  # Ｆａｌｓｅ不为空的
    #  正则表达式！
    bookinfo_regex = BookInfo.books1.filter(btitle__regex=r".*飞.*").count()
    # bookinfo_search =BookInfo.books1.filter(btitle__search="哈哈").count() # ???
    # pk__gt > | pk__gte >= | pk__lt  < | pk__lte <=
    bookinfo_in_count = BookInfo.books1.filter(pk__in=[1, 2, 3, 4, 5]).count()
    # bookinfo_year =BookInfo.books1.filter(bpub_date__year=2017)
    # 　只写和对象相关的字段，不写和数据库相关的字段
    bookinfo_yeargt = BookInfo.books1.filter(bpub_date__gt=date(year=1998, month=1, day=1)).count()
    bookinfo_yeargt = BookInfo.books1.filter(bpub_date__year='1980').count()
    bookinfo_yeargt = BookInfo.books1.filter(bpub_date__gt='1980-01-01').count()
    bookinfofilter = BookInfo.books1.filter(btitle__contains="天")  # filter first
    # bookinfoexact = BookInfo.books1.filter(btitle__exact="python编程") # 默认就是exact
    bookinfoexact = BookInfo.books1.filter(btitle="python编程")
    # 关联查询 heroinfo 表关联查询子表包含字符串八 查询出来的是ｂｏｏｋｉｎｆｏ对象
    #  关联模型类名小写__属性名__运算符=值  where 后面的条件，自动内连接
    #  一查多有外键 有外键优先使用外键作为关联的模型类小写
    bookinfo_inner_join = BookInfo.books1.filter(heroinfo__hcontent__contains="八")  # ???
    inner_join_1 = BookInfo.books1.filter(heroinfo__hname__startswith="黄")
    # 聚合函数
    # == >  {'bpub_date__max': datetime.datetime(2017, 12, 31, 16, 0, tzinfo=<UTC>)}
    max_date = BookInfo.books1.all().aggregate(Max("bpub_date"))  # ==> select max(pub_date) from bookinfo
    # ==> {'bread__avg': 11.4545}
    avg_bread = BookInfo.books1.all().aggregate(Avg("bread"))  # select avg(bread) from bookinfo
    # inner_join = BookInfo
    # 字段和字段相互比较需要用到 F对象
    f1 = BookInfo.books1.filter(bread=F("bcomment")).count()
    f2 = BookInfo.books1.filter(bread__gt=F("bcomment") * 2).count()
    f3 = BookInfo.books1.filter(isDelete=F("heroinfo__isDelete")).count()  # 字段和关联表的字段相等
    f4 = BookInfo.books1.filter(bpub_date=F("bpub_date") + timedelta(days=1))
    # 多个条件默认filter().filert() 是并且的关系,简写为，分割   filter(bread__contains="xxx",isDelete=True)
    # Q 对象表示逻辑与或者逻辑或的关系，逻辑与也可以写为 Q（pk__gt=5）& Q(isDelete=True)
    # Q 对象表示逻辑或关系 Q(pk__gt=5) |
    q1 = BookInfo.books1.filter(pk__gt=5, bcomment__gte=20)  # ==》 filter(pk__gt=5).filter(bcomment__gte=20)

    q2 = BookInfo.books1.filter(Q(pk__gt=5) | Q(btitle__contains="八")).count()
    q3 = BookInfo.books1.filter(~Q(pk=1)).count()
    q4 = BookInfo.books1.exclude(pk=1)  # 同上写法不一样
    context = {
        "bookinfo": bookinfo,
        "bookinfo_model": bookinfo_model,
        "bookinfo_exist": bookinfo_exist,
        "bookinfo_endwith_model": bookinfo_endwith_model,
        "bookinfo_isnotnull_count": bookinfo_isnotnull_count,
        "bookinfo_regex": bookinfo_regex,
        # "bookinfo_search": bookinfo_search,
        "bookinfo_in_count": bookinfo_in_count,
        "bookinfo_yeargt": bookinfo_yeargt,
        "bookinfofilter": bookinfofilter,
        "bookinfoexact": bookinfoexact,
        "bookinfo_inner_join": bookinfo_inner_join,
        "max_date": max_date,
        "avg_bread": [avg_bread][0]["bread__avg"],  # ==> 单个对象可以加【】变为可迭代对象临时处理 ==》"avg_bread":[avg_bread]
        "f1": f1,
        "f2": f2,
        "q1": q1,
        "q2": q2,
        "q3": q3,
        "inner_join_1": inner_join_1
    }
    return render(request, "booktest/select.html", context)


def area(request):
    # 获取石家庄
    area_shijiazhuang = Area.objects.get(pk=130100)
    # 第二种在后台传递到上下文
    # sheng = area_shijiazhuang.aPid
    # qu = area_shijiazhuang.area_set.all()
    context = {"area_shijiazhuang": area_shijiazhuang}
    return render(request, "booktest/area.html", context)


def request(request):
    if request.COOKIES:
        a = True
    else:
        a = False
    context = {
        "a": a,
        "request.path": request.path,
        "request.get_full_path": request.get_full_path(),
        "request.path_info": request.path_info,
        "request.method": request.method,
        # 默认None=>一般ｕｔｆ－８
        "request.encoding": request.encoding,
        "request.COOKIES": request.COOKIES,
        "request.GET": request.GET,  # 和请求方式无关，只获取？a=2&b=3....get参数
        "request.POST": request.POST,
        "request_session": request.session,
        "request_session_isajax": request.is_ajax(),
    }
    return render(request, "booktest/request.html", context)


def get_group_param(request, p1, p2, p3):
    # str_1 = p1 + p2 + p3  # 接过来都为字符串 仅仅是字符串拼接
    str_2 = "%s:%s:%s" % (p1, p2, p3)
    return HttpResponse(str_2)


def getTest1(request):
    context = {

    }
    return render(request, "booktest/getTest1.html", context)


def getTest2(request):
    a = request.GET["a"]
    b = request.GET["b"]
    c = request.GET["c"]
    d = request.GET.get("d", default="666")
    context = {
        "a": a,
        "b": b,
        "c": c,
        "d": d,
    }
    return render(request, "booktest/getTest2.html", context)


def getTest3(request):
    a1 = request.GET.get("a")  # 等同下句
    a1 = request.GET["a"]
    alist = request.GET.getlist("a")  # 一次全部取出，列表类型
    context = {
        "a1": a1,  # 一键多值取一个默认取最后一个
        "alist": alist
    }

    return render(request, "booktest/getTest3.html", context)


def postTest1(request):
    context = {}
    return render(request, "booktest/postTest1.html", context)  # 渲染自己的视图


def postTest2(request):
    # query_dict = request.POST
    name = request.POST["txtName"]
    password = request.POST["txtPassword"]
    gender = request.POST["gender"]
    hobby_list = request.POST.getlist("hobby")
    context = {
        "name": name,
        "password": password,
        "gender": gender,
        "hobby_list": hobby_list,

    }
    return render(request, "booktest/postTest2.html", context)


def ajax(request):
    return render(request, "booktest/ajax.html")


# @csrf_exempt
def ajax_request(request):
    # {"name":"pxd"}
    book_list = BookInfo.books1.all()

    my_dict = []
    for x in book_list:
        my_dict.append({"btitle": x.btitle, "bpub_date": x.bpub_date})
        # my_dict.append([x.btitle,x.bpub_date])
    my_data = {"data": my_dict}
    return JsonResponse(my_data)


def cookieTest(request):
    """
    cookie是基于网站隔离的
    设置 修改 操作cookie 用 response 对象
    获取 读取,cookie 用 request 对象
    set_cookie(key, value='', max_age=None, expires=None)：设置Cookie
    key、value都是字符串类型
    max_age是一个整数，表示在指定秒数后过期
    expires是一个datetime或timedelta对象，会话将在这个指定的日期/时间过期，注意datetime和timedelta值只有在使用PickleSerializer时才可序列化
    max_age与expires二选一
    如果不指定过期时间，则两个星期后过期

    """
    response = HttpResponseRedirect("/booktest/index")

    ret = request.COOKIES.get("my_name")
    print(ret)

    # if request.COOKIES.has_key('mark'):
    # # do something
    # response.set_cookie("my_name","666")
    # mycookie = request.COOKIES["key_name"] # 没有会报错
    # mycookie = request.COOKIES.get("key_name", "没有设置ｃｏｏｋｉｅ")
    # response.content = mycookie
    # response.set_cookie("key_name", "abc")
    # response.content = "ｏｋ"
    ## 请求request获取ｃｏｏｋｉｅ
    # httpresponse_model.content =  request.COOKIES["key_name"]
    ## 获取ｃｏｏｋｉｅ
    # httpresponse_model.write(request.COOKIES["key_name"])

    # ＃ 设置response cookie
    # response.set_cookie("key_name", "12345",60)
    # response.set_cookie("key_name", "654321", None, datetime(2018, 1, 20))
    ## 删除ｃｏｏｋｉｅ
    # response.delete_cookie("key_name")
    return response


def redirect1(request):
    """
    反向解析 传递位置参数
    {% url "main:index" 18 188%}

    反向解析传递命名参数 2 种都可以
    {% url "main:index" 18 188%}
    {% url "main:index" param1=18 param2=188%}

    r"/index/(?P<param1>\d+)/(?P<param2>\d+)/"
    :param request:
    :return:
    """
    # 反向解析需要的reverse
    # from django.core.urlresolvers import reverse
    ##　重定向１
    # return HttpResponseRedirect("/booktest/")  # url 地址
    # return HttpResponseRedirect(reverse("index"))  #  ok
    return HttpResponseRedirect(reverse("main:index"))  # ok
    #  反向解析传递位置参数
    args = (18, 188)
    # return redirect(reverse("main:index"),*args)
    # return redirect(reverse("main:index"),args=(18,188))
    #  反向解析传递命名参数 2 种都可以
    return redirect(reverse("main:index"), kwargs={"param1": "aaa", "param2": "bbb"})
    return redirect(reverse("main:index"), args=("aaa", "bbb"))
    dict = {"param1": "aaa", "param2": "bbb"}
    return redirect(reverse("main:index"), **dict)
    # return HttpResponseRedirect(reverse("postTest1"))
    ## 　重定向２

    # return redirect(reverse('main:index'))
    # return redirect(reverse("main:login"))  # 反向解析

    #  反向解析传参，元祖默认一个参数加逗号
    return HttpResponseRedirect(reverse('booktest:index2', args=(1,)))
    # return redirect()

    ## json格式


# return JsonResponse({"name": "pxd", "age": 18, "gender": "男"})


def redirectTest1(request):
    context = {}
    return render(request, "booktest/redircectTest1.html", context)


import django.template


def session_test(request):
    request.session["lll"] = 111
    value = request.session.get("lll", "session没有值哟")
    return HttpResponse(value)


def session1(request):
    # request.session.has_key("s_name")
    request.session["name"] = "666"
    value = request.session.get("lll", "session没有值哟")
    context = {
        "name": value,
    }
    return render(request, "booktest/session1.html", context)


def session2(request):
    # 直接跳转页面什么也不传
    return render(request, "booktest/session2.html")


def session2_handle(request):
    txtName = request.POST["txtName"]
    # 设置ｓｅｓｓｉｏｎ的值
    request.session["name"] = txtName
    # 设置session 的超时时间
    # request.session.set_expiry(10)# 10 秒后过期
    # request.session.set_expiry(timedelta(days=5)) # 5天后过期
    # 反
    # request.session.set_expiry(None)  # 设置为None 永不过期
    request.session.set_expiry(0)  # 设置为0 关闭浏览器就过期，失效
    # return redirect("/booktest/session1/")
    return HttpResponseRedirect("/booktest/session1/")


def session2_delete(request):
    """删除session的 4 种方式"""
    # 4种删除ｓｅｓｓｉｏｎ方式
    request.session["name"] = None
    # del request.session["name"]
    # request.session.clear()
    # request.session.flush()
    #  jj = HttpResponse()

    return HttpResponseRedirect("/booktest/session1/")


def login(request):
    name = request.session.get("name", "没有session")
    context = {
        "name": name,
        "array": [1, 2, 3, 4],
        "dic": {"name": "ppd", "age": 18}
    }
    return render(request, "booktest/login.html", context)


def set_session(request):
    txtName = request.POST["txtName"]
    request.session["name"] = txtName
    # return HttpResponseRedirect("/booktest/login/")
    return redirect(reverse("main:login"))


def del_session(request):
    del request.session["name"]
    # request.session["name"] = None
    # request.session.clear()
    # request.session.flush()
    # return HttpResponseRedirect("/booktest/login")
    return redirect(reverse("main:login"))


def empty_eg(request):
    list = BookInfo.books1.filter(pk__gt=0).all()
    dt = BookInfo.books1.filter(pk__exact=1).first().bpub_date
    context = {
        "list": list,
        "dt": dt
    }

    return render(request, "booktest/empty_eg.html", context)


def show_eg(request, id1, id2, id3):
    return render(request, "booktest/show_eg.html", {"id1": id1, "id2": id2, "id3": id3})


def baseTemplate(request):
    return render(request, "booktest/baseTemplate.html")


def indexInherit(request):
    return render(request, "booktest/indexInherit.html")


def baseUser(request):
    return render(request, "booktest/baseUser.html")


def baseGoods(request):
    return render(request, "booktest/baseGoods.html")


def userInherit1(request):
    context = {
        # "user_name": "测试user_name" # 传惨给前台
    }
    return render(request, "booktest/userInherit1.html", context)


def htmlTest(request):
    """自动转义"""
    context = {
        "html": "<ul><li>1<li></ul>"
    }
    # return HttpResponse("<h1>aaaa</h1>") # 会展示出html不会转义为普通字符串
    return render(request, "booktest/htmlTest.html", context)  # 会被转义为字符串


# csrf跨站请求伪造
def csrf1(request):
    return render(request, "booktest/csrf1.html")


def csrf2(request):
    uname = request.POST.get("uname")
    context = {"uname": uname}
    return render(request, "booktest/csrf2.html", context)


# 验证码
def verifyCode(request):
    from PIL import Image, ImageDraw, ImageFont
    import random
    # 创建背景色
    bgColor = (random.randrange(50, 100), random.randrange(50, 100), 0)
    width = 100
    height = 25
    # 创建画布
    image = Image.new("RGB", (width, height), bgColor)
    # 构造字体对象
    font = ImageFont.truetype("FreeMono.ttf", 25)
    # 创建画笔
    draw = ImageDraw.Draw(image)
    # 创建文本内容
    text = "ABCD1234abcd"
    text_temp = ''  # 外面一个变量暂存
    for i in range(4):
        texttemp1 = text[random.randrange(0, len(text))]  # random.randomrange 是左闭右开的
        text_temp += texttemp1
        draw.text((i * 25, 0), texttemp1, (255, 255, 255), font)

    request.session["code"] = text_temp
    # 逐个绘制字符
    # for item in text:
    # draw.text((0, 0), text, (255, 255, 255), font)
    # 内存文件ＩＯ操作
    import cStringIO
    buffer = cStringIO.StringIO()
    image.save(buffer, "png")

    return HttpResponse(buffer.getvalue(), "image/png")


def verifycode_teacher(request):
    # 引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象
    font = ImageFont.truetype('FreeMono.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def form_validate_code(request):
    return render(request, "booktest/form_validate_code.html")


def form_recv(request):
    uname = request.POST.get("uname")
    code = request.session.get("code")
    return render(request, "booktest/form_recv.html", {"uname": uname.upper(), "code": code.upper()})


def static_picture(request):
    return render(request, "booktest/static_picture.html")


def show_exception(request):
    num = 1 / 0
    return HttpResponse(num)


def show_upload(request):
    return render(request, "booktest/show_upload.html")


# 上传接收方法
def recv_upload(request):
    """
    ImageField ==》  varchar类型主要用于后台站点上传，存储路径为upload to 的地址Booktest/1.png
    迁移文件存储表 django_migrations
    尽量保证（新的项目）新的迁移文件和表中不一致，
    choice no 就会创建新表而不会删除原有表

    """
    # 接收file文件流 request.FILES["name"]  | request.FILES.get("name")
    file = request.FILES.get("pic")
    path = os.path.join(settings.MEDIR_ROOT, "booktest")  # 获取settings.py中的全局变量,获取路径
    file_name = file.name  # 文件名
    file_ext_name = file_name.split(".")[1]
    new_file_name = (str(random.randrange(1, 99999999)) + "." + file_ext_name)
    full_path_name = os.path.join(path, new_file_name)
    with open(full_path_name, "ab") as f:  # wb 有问题! 不能用wb
        for item in file.chunks():  # 以安全守护的形式取遍历，避免大文件造成内存溢出
            f.write(item)
    pic = PictureInfo()
    # settings.MEDIR_ROOT
    pic.path = "booktest/" + new_file_name
    pic.save()
    #  最后将图片的路径存储到数据库中，具体省略
    # http://127.0.0.1:8000/static/booktest/1.png
    # return HttpResponse(path_and_file_name)  # 测试上传地址是否正确
    # == > 这里上传成功以后路径是localhost:8000/static/upload/xxxx.jpg
    # 1. 普通写死的路径
    return HttpResponse("""<img src="/static/upload/booktest/%s" />""" % new_file_name)
    # 2.反向解析的路径 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 只能在模板中用!
    # return HttpResponse("<img src='{% static upload/"+new_file_name+" %}' />""")
    # return render(request, "booktest/recv_upload.html")


# 分页功能Q
def page_show(request, num):
    from  django.core.paginator import Paginator

    if not num:
        num = 1
    sheng_list = AreaInfo.objects.filter(pk__gte=0)
    pageinator_model = Paginator(sheng_list, 10)  # 分页所有数据,每页显示10个
    page_model = pageinator_model.page(num)
    context = {
        "page_model": page_model
    }

    return render(request, "booktest/page_show.html", context)


def page_bar_helper_show(request):
    sheng_list = AreaInfo.objects.all()
    pageinator_model = Paginator(sheng_list, 10)  # 分页所有数据,每页显示10个
    num = request.GET.get("pageIndex")
    if not num:
        num = 1
    page_model = pageinator_model.page(num)
    # print page_model.number
    # print type(page_model.number)
    # print pageinator_model.count
    # print type(page_model.count)
    # print pageinator_model.num_pages
    # print type(pageinator_model.num_pages)
    import PageBarHelper
    page_bar_html = PageBarHelper.PageBarHelper.get_page_bar(page_model.number, pageinator_model.num_pages, 5)
    context = {
        "page_model": page_model,
        "page_bar_html": page_bar_html,
    }
    return render(request, "booktest/page_bar_helper_show.html", context)


# """分页功能"""
def pageinator_page(request, page_index):
    """
    Page对象
    number属性：返回当前是第几页
    paginator属性: 返回paginator 对象
    object_list属性: 返回当前页对象的列表
    len():返回当前页对象的个数
    has_next()：如果有下一页返回True
    has_previous()：如果有上一页返回True
    has_other_pages()：如果有上一页或下一页返回True
    next_page_number()：返回下一页的页码，如果下一页不存在，抛出InvalidPage异常
    previous_page_number()：返回上一页的页码，如果上一页不存在，抛出InvalidPage异常
    :param request:
    :param page_index:第几页
    :return:
    """
    # 空字符串或者是None 设置为第一页
    if not page_index:
        page_index = 1
    # 如果需要通过page对象找到pageinator对象可以直接点出来!! page_model.paginator
    book_list = BookInfo.books1.all()
    pageinator_model = Paginator(book_list, 5)  # 放入类list对象就可以分页

    # 页码列表
    pageinator_range = pageinator_model.page_range
    # 总页数  第一种写法，由于pageinator和page都是可以遍历的对象所以也可以.count
    pageinator_model_count = pageinator_model.count  # 属性
    # num_pages 页面总数,一共分了多少页
    pageinator_num_pages = pageinator_model.num_pages  # 属性

    # 返回page_model 可直接遍历
    page_model = pageinator_model.page(int(page_index))  # '1'  | 1
    # 当前页上所有对象的列表 也可直接遍历page_model省取object_list
    page_model_object_list = page_model.object_list
    # 当前页 从1 开始  不同于数组索引
    page_model_number = page_model.number
    # 求当前页有多少条记录数
    len_page_model = len(page_model)
    page_model_endindex = page_model.end_index()
    page_model_next_page_number = page_model.next_page_number()  # 返回下一页 的数字没有下一页报错！
    # page_model_count = page_model.count(1) # pagemodel 中1出现的次数！
    context = {
        "pageinator_model": pageinator_model,
        "pageinator_model_count": pageinator_model_count,  # 总页数
        "pageinator_range": pageinator_range,  # 页码列表
        "page_model": page_model,  # 当前页对象,可以遍历
        "page_model_object_list": page_model_object_list,
        "page_model_number": page_model_number,  # 当前页码条
        "page_index": page_index,
        "len_page_model": len_page_model,  # 求当前页有多少条记录数
        "page_model_endindex": page_model_endindex  # 返回本页最后一条记录是所有记录中第几个
    }
    return render(request, "booktest/pageinator_page.html", context)


def sheng_shi_lian_dong(request):
    context = {}
    return render(request, "booktest/sheng_shi_lian_dong.html", context)


# 百度解决方案  post 取消 csrf 校验
# from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
def getSheng(request, param_id):
    province_id = int(param_id)
    if province_id == 0:
        all_province_list = AreaInfo.objects.filter(areaPid__isnull=True)  # .values("id", "areaTitle")
    else:
        all_province_list = AreaInfo.objects.filter(areaPid__exact=province_id)

    # my_list = all_province_list
    my_list = []
    for item in all_province_list:
        my_list.append([item.id, item.areaTitle])  # 第一种方式返回json数据
        # my_list.append({"id": item.id, "areaTitle": item.areaTitle})  # 第二种方式返回数据
    my_data = {"data": my_list}

    return JsonResponse(my_data)


@csrf_exempt
def getShengDict(request, param_id):
    """字典方式返回jsonresponse"""
    province_id = int(param_id)
    if province_id == 0:
        all_province_list = AreaInfo.objects.filter(areaPid__isnull=True)
    else:
        all_province_list = AreaInfo.objects.filter(areaPid__exact=province_id)

    my_list = []
    for item in all_province_list:
        my_list.append({"id": item.id, "areaTitle": item.areaTitle})
    my_data = {"data": my_list}  # 必须组织为字典
    return JsonResponse(my_data)


# 不通过url 通过POST传递参数的方式
@csrf_exempt
def getShengByParameter(request):
    province_id = int(request.POST.get("id"))
    if province_id == 0:
        all_province_list = AreaInfo.objects.filter(areaPid__isnull=True)
    else:
        all_province_list = AreaInfo.objects.filter(areaPid__exact=province_id)

    my_list = []
    for item in all_province_list:
        my_list.append({"id": item.id, "areaTitle": item.areaTitle})
    my_data = {"data": my_list}  # 组织为字典
    return JsonResponse(my_data)  # 返回的是my_data的值


# 错误写法 values
@csrf_exempt
def getShengError(request, param_id):
    # import json
    # json_str=json.dump(xx)
    province_id = int(param_id)
    if province_id == 0:
        all_province_list = AreaInfo.objects.filter(areaPid__isnull=True).values("id", "areaTitle")

    return HttpResponse(all_province_list)


def tinymce(request):
    return render(request, "booktest/tinymce.html", {})


def save_tinymce(request):
    comment = request.POST["comment"]
    tiny = TinyMce()
    tiny.comment = comment
    tiny.save()
    context = {"comment": comment}
    return render(request, "booktest/save_tinymce.html", context)


# @cache_page(10)
def cache_show(request):
    book_list = BookInfo.books1.filter(pk__exact=1)
    # 设置底层数据缓存 存储导redis 中
    # cache.set("my_key", "my_value", 600)
    # print(cache.get("my_key"))
    cache.clear()
    context = {"book_list": book_list}
    return render(request, "booktest/cache_show.html", context)


# from django.core.cache import cache  # 更改配置后同样用于redis
# 设置：cache.set(键,值,有效时间)
# 获取：cache.get(键)
# 删除：cache.delete(键)
# 清空：cache.clear()


# 单个视图缓存
# from django.views.decorators.cache import  cache_page
@cache_page(60)
# 最原始的写法  接受请求逻辑处理 套用模板 相应html
def chuan_tong(request):
    # settings.py里配置了模板搜索文件夹路径但是这里还需要指明是哪个模块的,可能有多个模块
    template_model = loader.get_template("booktest/test.html")  # 加载模板
    context = RequestContext(request, {"testdata": "测试数据"})  # 准备数据
    #                                  渲染模板
    return HttpResponse(template_model.render(context=context, request=request))


# 全文检索+中文分词
def jiebasearch(request):
    return render(request, "booktest/jiebasearch.html", {})


# from task import *
# celery 异步调用
def use_celery(request):
    # show()
    show.delay()
    return HttpResponse("ok")
