#前端子路由文件
from django.contrib import admin
from django.urls import path,include
from web.views import index,cart,orders
urlpatterns = [
    path('', index.index, name="index"),
   
    #前台的登录退出的路由
     path('login', index.login, name="web_login"),#加载登录表单
     path('dologin', index.dologin, name="web_dologin"),#登录
     path('logout', index.logout, name="web_logout"),#退出
     path('verify', index.verify, name="web_verify"),#退出

     #为url路由添加请求前缀web/,凡是带有web前缀的需要登录才能进入
     path("web/",include([
         path('',index.webindex,name="web_index"),#前台大堂点餐首页
         #购物车信息管理路由
         path('cart/add/<str:pid>',cart.add,name="web_cart_add"),#购物车添加
         path('cart/delete/<str:pid>',cart.delete,name="web_cart_delete"),#购物车删除
         path('cart/clear',cart.clear,name="web_cart_clear"),#购物车添加
         path('cart/change',cart.change,name="web_cart_change"),#购物车修改



        #订单处理路由
        path('orders/insert',orders.insert,name="web_orders_insert"),#订单添加
        path('orders/<int:pIndex>',orders.index,name="web_orders_index"),#订单浏览
        path('orders/detail',orders.detail,name="web_orders_detail"),#订单详情
        path('orders/status',orders.status,name="web_orders_status"),#修改订单状态
        
         
         
     ]))
    
]
