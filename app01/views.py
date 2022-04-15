from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
	res = {
		"code": 0,
		"msg": "成功success！",
		"data": []
	}
	# return HttpResponse("hello, world!")
	return JsonResponse(res, json_dumps_params={"ensure_ascii": False})

def hellow(request):
	context = {}
	context['hello'] = "Hello, World!你好，世界！"
	# return render(request, "hello.html", context)

	# 模板语法
	# view：｛"HTML变量名" : "views变量名"｝
	# HTML：｛｛变量名｝｝
	# 以下两种均可以
	# return render(request, "hello.html", {"name": "ok"})
	# view_name = "ok"
	# return render(request, "hello.html", {"name": view_name})

	# name = []时
	# view_name = ["张三", "李四", "王五"]
	# return render(request, "hello.html", {"name": view_name})   # 取全部name
	# return render(request, "hello.html", {"name": view_name})

	# name = {}时
	# person = {"name": "Zhangsan张三", "age": "25", "birthday":"1990-10-31 03:34:56"}
	# return render(request, "hello.html", {"person": person})

	# 管道带参数
	name = ["Zhangsan", "Lihua", "1990-10-31 03:34:56"]
	return render(request, "hello.html", {"name": name})