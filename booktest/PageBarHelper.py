# -*- coding:utf-8 -*-

class PageBarHelper(object):
    @classmethod
    def get_page_bar(cls, pageIndex, pageCount, each_page_show=10):
        """
        :param pageIndex: 当前页
        :param pageCount: 总页数
        :return:
        """
        if pageCount == 1:
            return ""
        start = pageIndex - (each_page_show / 2)  # 计算起始位置 默认要求页面显示10个页码总共
        if start < 1:
            start = 1
        end = start + (each_page_show - 1)
        if end > pageCount:
            end = pageCount
            # 重新计算start
            start = end - (each_page_show - 1) if end - (each_page_show - 1) > 0 else 1
        page_bar_html = ""
        # 首页
        page_bar_html += "<a href='?pageIndex=1'>首页</a>&nbsp;"
        # 如果是第一页不显示“上一页  可选项”
        if pageIndex > 1:
            page_bar_html += "<a href='?pageIndex=%s'>上一页</a>&nbsp;" % (pageIndex - 1)
        # 添加数字页码条
        for i in range(start, end + 1):
            if i == pageIndex:
                page_bar_html += str(i) + "&nbsp;"
            else:
                page_bar_html += "<a href='?pageIndex=%s'>%s</a>&nbsp;" % (i, i)
        # 如果是最后一页不显示上一页 可选项
        if pageIndex < pageCount:
            page_bar_html += "<a href='?pageIndex=%s'>下一页</a>&nbsp;" % (pageIndex + 1)
        # 末页
        page_bar_html += "<a href='?pageIndex=%s'>末页</a>&nbsp;" % (pageCount)
        return page_bar_html

    @classmethod
    def t(cls):
        return "行业人才666"
