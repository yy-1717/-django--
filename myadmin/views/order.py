#会员信息管理的视图文件
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
# Create your views here.
from myadmin.models import Order,Shop
from datetime import datetime
import hashlib,random

def index(request,pIndex=1):
    '''浏览信息'''
    umod = Order.objects
    ulist = umod.filter(status__lt=3)
    mywhere = []
    #获取，判断并封装状态status搜索条件
    status = request.GET.get('status','')
    if status !='':
        ulist = ulist.filter(statua=status)
        mywhere.append("status="+status)
   #执行分页处理
    pIndex = int(pIndex)
    page = Paginator(ulist,10) #每页五条数据分页
    maxpages = page.num_pages  #获取最大页数s
    #判断当前页是否越界
    if pIndex >maxpages :
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex) #获取当前页数据
    plist = page.page_range #获取页码列表信息
    context = {"orderlist":list2,'plist':plist,'pIndex':pIndex,'maxpages':maxpages,'mywhere':mywhere}
    return render(request,"myadmin/order/index.html",context)

def delete(request,oid=0):
    '''执行信息删除'''
    try:
        ob = Order.objects.get(id=oid)
        ob.status = 3 
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info':"删除成功！"}
    except Exception as err:
        print(err)
        context = {'info':"删除失败！"}
    return render(request,"myadmin/info.html",context)
def edit(request,oid=0):
    '''加载信息编辑表单'''
    try:
        ob = Order.objects.get(id=oid)
        context = {'order':ob}
        return render(request,"myadmin/order/edit.html",context)
    except Exception as err:
        print(err)
        context = {'info':"没有找到要修改的信息！"}
        return render(request,"myadmin/info.html",context)
def update(request,oid=0):
    '''执行信息修改'''
    try:
        ob = Order.objects.get(id=oid)
        ob.name = request.POST['name']
        ob.status = request.POST['status']
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info':"修改成功！"}
    except Exception as err:
        print(err)
        context = {'info':"修改失败！"}
    return render(request,"myadmin/info.html",context)
