#菜品类别信息管理的视图文件
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.paginator import Paginator
# Create your views here.
from myadmin.models import Category,Shop
from datetime import datetime


def index(request,pIndex=1):
    '''浏览信息'''
    umod = Category.objects
    ulist = umod.filter(status__lt=9)
    mywhere = []
    #获取并判断搜索条件
    kw = request.GET.get("keyword",None)
    if kw:
        ulist = ulist.filter(name__contains=kw)
        mywhere.append('keyword='+kw)
    #获取，判断并封装状态status搜索条件
    status = request.GET.get('status','')
    if status !='':
        ulist = ulist.filter(statua=status)
        mywhere.append("status="+status)
   #执行分页处理
    pIndex = int(pIndex)
    page = Paginator(ulist,5) #每页五条数据分页
    maxpages = page.num_pages  #获取最大页数
    #判断当前页是否越界
    if pIndex >maxpages :
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex) #获取当前页数据
    plist = page.page_range #获取页码列表信息
    
    #遍历当前菜品分类信息并封装
    for vo in list2:
        sob = Shop.objects.get(id=vo.shop_id)
        vo.shopname = sob.name

    context = {"categorylist":list2,'plist':plist,'pIndex':pIndex,'maxpages':maxpages,'mywhere':mywhere}
    return render(request,"myadmin/category/index.html",context)

def add(request):
    '''加载信息添加信息'''
    slist = Shop.objects.values("id",'name')
    context = {"shoplist":slist}
    return render(request,"myadmin/category/add.html",context)

def insert(request):
    '''执行信息添加'''
    try:
        ob = Category()
        ob.shop_id = request.POST['shop_id']
        ob.name = request.POST['name']
        ob.status = 1
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info':"添加成功！"}
    except Exception as err:
        print(err)
        context = {'info':"添加失败！"}
    return render(request,"myadmin/info.html",context)
def delete(request,cid=0):
    '''执行信息删除'''
    try:
        ob = Category.objects.get(id=cid)
        ob.status = 9 
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info':"删除成功！"}
    except Exception as err:
        print(err)
        context = {'info':"删除失败！"}
    return render(request,"myadmin/info.html",context)
def edit(request,cid=0):
    '''加载信息编辑表单'''
    try:
        ob = Category.objects.get(id=cid)
        context = {'category':ob}
        slist = Shop.objects.values("id",'name')
        context["shoplist"] = slist
        return render(request,"myadmin/category/edit.html",context)
    except Exception as err:
        print(err)
        context = {'info':"没有找到要修改的信息！"}
        return render(request,"myadmin/info.html",context)
def update(request,cid=0):
    '''执行信息修改'''
    try:
        ob = Category.objects.get(id=cid)
        ob.name = request.POST['name']
        ob.status = request.POST['status']
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info':"修改成功！"}
    except Exception as err:
        print(err)
        context = {'info':"修改失败！"}
    return render(request,"myadmin/info.html",context)

def loadCategory(request,sid):
    clist = Category.objects.filter(status__lt=9,shop_id=sid).values("id","name")
    return JsonResponse({'data':list(clist)})