from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

class MiddleWareTest(MiddlewareMixin):
    def process_request(self,request):
        request_ip=request.META["REMOTE_ADDR"]
        if request_ip=="10.10.14.172":
            return HttpResponse("不让你进")
#     def process_view(self,request,callback,callback_args,callback_kwargs):
#         print("i am view 方法")
#         return "i am view"



import logging
#DEBUG  INFO WARNING ERROR CRITICAL

logging_header=logging.FileHandler("test.log",encoding='utf-8')
stream_header=logging.StreamHandler()

log_format="%(asctime)s【%(levelname)s】%(message)"
time_format=""