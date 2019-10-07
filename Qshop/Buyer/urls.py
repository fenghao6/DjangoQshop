from django.urls import path,include,re_path
from Buyer.views import *

urlpatterns = [
    path('login/', login),
    path('register/', register),
    path('index/', index),
    path('logout/', logout),
    path('goods_list/', goods_list),
    re_path('goods_detail/(?P<id>\d+)',goods_detail),
    path("user_info/",user_center_info),
    path("pay_order/",pay_order),

    path("pay_order_more/",pay_order_more),

    path("alipay/",Alipayviews),
    path("pay_result/",pay_result),
    path("add_cart/",add_cart),
    path("cart/",cart),
    path('uco/',user_center_order),
    path('gt/', get_task),
    # path('mtv/',middle_test_view),


]
