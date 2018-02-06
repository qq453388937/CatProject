# -*- coding:utf-8 -*-
from django.template import Library

register = Library()  # 必须叫ｒｅｇｉｓｔｅｒ


# @register.tag
# @register.tag_function
@register.filter
def mod(param):
    """判断单双"""
    # if param % 2 == 0:
    #     return True
    # else:
    #     return False
    return param % 2


@register.filter
def mod1(param1, param2):
    """判断单双多参数"""
    # if param % 2 == 0:
    #     return True
    # else:
    #     return False
    return param1 % param2
