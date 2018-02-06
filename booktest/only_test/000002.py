# -*- coding:utf-8 -*-

class PageBarHelper(object):
    @classmethod
    def get_page_bar(cls, pageIndex, pageCount):
        """
        :param pageIndex: 当前页
        :param pageCount: 总页数
        :return:
        """
        if pageCount == 1:
            return ""
        start = pageIndex - 5  # 计算起始位置 默认要求页面显示10个页码总共
        if start < 1:
            start = 1
        end = start + 9
        if end > pageCount + 9:
            end = pageCount
            # 重新计算start
            start = end - 9 if end - 9 > 0 else 1
        page_bar_html = ""
        # 如果是第一页不显示“上一页”
        if pageIndex > 1:
            page_bar_html += "<a href=/booktest/page_show%s/>上一页</a>" % (pageIndex - 1)
        # 添加数字页码条
        for i in range(start, end):
            if i == pageIndex:
                page_bar_html += str(i)
            else:
                page_bar_html += "<a href=/booktest/page_show%s/>%s</a>" % (i, i)
        # 如果是最后一页不显示上一页
        if pageIndex < pageCount:
            page_bar_html += "<a href=/booktest/page_show%s/>下一页</a>" % (pageIndex + 1)
        return page_bar_html

# end = 22
# start = end - 9 if end - 9 > 0 else 1  # end-9>0 ? end-9:1
# print startPageBarHelper


print(PageBarHelper.get_page_bar(3, 10))
