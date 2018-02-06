# coding=utf-8
from django.conf.urls import url  # include,
# from  . import views  ==>  url(r"^$|^index", views.index),
# from .views import *  ==>  url(r"^$|^index", index),
# from  views import *
# from booktest.views import *  # url的第二个参数不用模块名点
# from  booktest import views
import views
import views7777777

# index
urlpatterns = [
    url(r"^select$/", views.select, name="select"),
    url(r"^test/$", views.test, name="test"),
    url(r"^$|^index/$", views.index, name="index"),
    url(r"^old_response$", views.old_response),
    url(r"^chuan_tong/$", views.chuan_tong),
    url(r"^new_style$", views.new_style),
    url(r"^(\d+)$", views.show_new_detail2),

    url(r"^area/$", views.area, name="area"),  # name??  反向解析
    url(r"^print_(\d+)$", views.printf_ids),
    url(r"^print_ids/(\d+)/(\d+)/(\d+)$", views.print_ids, name="print_ids"),
    url(r"^print_group_ids/(?P<myid>\d+)/(?P<secondid>\d+)/(?P<thirdid>\d+)$", views.print_group_ids),
    url(r"^views7777777$", views7777777.index, name="views7777777"),
    url(r"^(?P<p2>\d+)/(?P<p3>\d+)/(?P<p1>\d+)/", views.get_group_param),
    url(r"^request/$", views.request, name="request"),
    url(r"^getTest1/$", views.getTest1),
    url(r"^getTest2/$", views.getTest2),
    url(r"^getTest3/$", views.getTest3),
    url(r"^postTest1/$", views.postTest1, name="postTest1"),
    url(r"^postTest2/$", views.postTest2),
    url(r"^cookieTest/$", views.cookieTest),
    url(r"^redirect1/$", views.redirect1, name="redirect1"),
    url(r"^redirectTest1/$", views.redirectTest1, name="redirectTest1"),
    url(r"^session1/$", views.session1, name="session1"),
    url(r"^session2/$", views.session2, name="session2"),
    url(r"^session2_handle/$", views.session2_handle, name="session2_handle"),
    url(r"^session2_delete/$", views.session2_delete, name="session2_delete"),
    url(r"^login/$", views.login, name="login"),
    url(r"^set_session/$", views.set_session, name="set_session"),
    url(r"^del_session/$", views.del_session, name="del_session"),
    url(r"^empty_eg/$", views.empty_eg, name="empty_eg"),
    # url(r"^eg/(\d+)/$", views.show_eg, name="show_eg"),
    url(r"^eg/(\d+)/(\d+)/(\d+)$", views.show_eg, name="show_eg"),
    url(r"^baseTemplate/$", views.baseTemplate, name="baseTemplate"),
    url(r"^indexInherit/$", views.indexInherit, name="indexInherit"),
    url(r"^baseUser$/", views.baseUser, name="baseUser"),
    url(r"^baseGoods$/", views.baseGoods, name="baseGoods"),
    url(r"^userInherit1/$", views.userInherit1, name="userInherit1"),
    url(r"^htmlTest/$", views.htmlTest, name="htmlTest"),
    url(r"^csrf1/$", views.csrf1, name="csrf1"),
    url(r"^csrf2/$", views.csrf2, name="csrf2"),
    url(r"^verifyCode/$", views.verifyCode, name="verifyCode"),
    url(r"^verifycode_teacher/$", views.verifycode_teacher, name="verifycode_teacher"),
    url(r"^form_validate_code/$", views.form_validate_code, name="form_validate_code"),
    url(r"^form_recv/$", views.form_recv, name="form_recv"),
    url(r"^static_picture/$", views.static_picture, name="static_picture"),
    url(r"^show_exception/$", views.show_exception, name="show_exception"),
    url(r"^show_upload/$", views.show_upload, name="show_upload"),
    url(r"^recv_upload/$", views.recv_upload, name="recv_upload"),
    # \d+ 改为\d*  最后一个/ 改为 /*
    url(r"^pageinator_page/(?P<page_index>\d*)/*$", views.pageinator_page, name="pageinator_page"),
    url(r"^sheng_shi_lian_dong/$", views.sheng_shi_lian_dong, name="sheng_shi_lian_dong"),
    url(r"^getSheng/(\d+)/$", views.getSheng, name="getSheng"),
    url(r"^getShengError/(\d+)/$", views.getShengError, name="getShengError"),
    url(r"^getShengDict/(\d+)/$", views.getShengDict, name="getShengDict"),
    url(r"^getShengByParameter/$", views.getShengByParameter, name="getShengByParameter"),
    url(r"^tinymce/$", views.tinymce, name="tinymce"),
    url(r"^save_tinymce/$", views.save_tinymce, name="save_tinymce"),
    url(r"^cache_show/$", views.cache_show, name="cache_show"),
    url(r"^jiebasearch/$", views.jiebasearch, name="jiebasearch"),
    url(r"^use_celery/$", views.use_celery, name="use_celery"),
    url(r"^ajax/$", views.ajax, name="ajax"),
    url(r"^ajax_request/$", views.ajax_request, name="ajax_request"),
    url(r"^session_test/$", views.session_test, name="session_test"),
    url(r"^page_show(\d*)/$", views.page_show, name="page_show"),
    url(r"^/$", views.page_bar_helper_show, name="page_bar_helper_show"),

    # save_tinymce cache_show use_celery  session_test  page_show  page_bar_helper_show
    # getSheng  getShengError  getShengDict shengAgain getShengByParameter
    # tinymce
    # url(r"^new_styles/(\d+)$", views.show_new_detail), # ?
    # url(r"^showdetail$", views.showdetail),
]
