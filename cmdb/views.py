from django.shortcuts import render
from cmdb import models
# from django.shortcuts import HttpResponse
# Create your views here.

#定义用户信息列表，预定义两个数据，它将被返回给浏览器，展示给用户
# user_list = [
# 	{"user":"jack","pwd":"abc"},
# 	{"user":"tom","pwd":"ABC"},
# ] 


def index(request):
	# request.POST
	# request.GET
	# return HttpResponse("Hello world!")
	if request.method=="POST":
		username = request.POST.get("username",None)
		password = request.POST.get("password",None)
		# print(username,password)
		# temp = {"user":username,"pwd":password}
		# user_list.append(temp)

		#添加用户数据到数据库
		models.UserInfo.objects.create(user=username,pwd=password)
	#从数据库读取所有数据
	user_list = models.UserInfo.objects.all()

	return render(request,"index.html",{"data":user_list})  #参数一固定，参数二为指定文件,参数三为字典（data是自定义指针名字，会被对应的html文件引用）