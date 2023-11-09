#移动端子路由文件
from django.contrib import admin
from django.urls import path
from mobile.views import index,member,cart
urlpatterns = [
    path('', index.index, name="mobile_index"),#移动端首页
    #会员注册/登录
    path('register', index.register, name="mobile_register"),#移动端会员注册/登录表单页
    path('doregister', index.doregister, name="mobile_doregister"),#执行注册或登录
    #店铺选择
    path('shop', index.shop, name="mobile_shop"),#移动端店铺选择
    path('shop/select', index.selectShop, name="mobile_selectshop"),#执行移动端店铺选择
    #购物车信息管理路由
  
    path('cart/add',cart.add,name="mobile_cart_add"),#购物车添加
    path('cart/delete',cart.delete,name="mobile_cart_delete"),#购物车删除
    path('cart/clear',cart.clear,name="mobile_cart_clear"),#购物车添加
    path('cart/change',cart.change,name="mobile_cart_change"),#购物车修改


    #订单处理
    path('orders/add', index.addOrders, name="mobile_addorders"),#移动端订单处理
    path('orders/doadd', index.doAddOrders, name="mobile_doaddorders"),#执行移动端订单处理
    #会员中心
     path('member', member.index, name="mobile_member_index"),#会员首页
     path('member/orders', member.orders, name="mobile_member_orders"),#会员订单处理
     path('member/detail', member.detail, name="mobile_member_detail"),#会员细节订单处理
     path('member/logout', member.logout, name="mobile_member_logout"),#会员登出处理


]
