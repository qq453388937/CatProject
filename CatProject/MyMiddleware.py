# -*- coding:utf-8 -*-


class MyMiddleware(object):
    def __init__(self):
        print('--------------init')

    def process_request(self, request):
        print('--------------request')

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('--------------view')

    def process_template_response(self, request, response):
        print('--------------template')
        return response

    def process_response(self, request, response):
        print('--------------response1111')
        response.set_cookie("aaaaaaaaaaaaaaaa", "bbbbbbbbbbbbbbbbbbb")
        return response

        # def process_exception(request, exception):
        #     pass
