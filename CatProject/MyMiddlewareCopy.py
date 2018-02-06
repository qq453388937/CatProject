# -*- coding:utf-8 -*-


class MyMiddleware(object):

    def process_response(self, request, response):
        print('--------------response2222222222222Copy')
        response.set_cookie("aaaaaaaaaaaaaaaa","bbbbbbbbbbbbbbbbbbb")
        return response

    # def process_exception(request, exception):
    #     pass