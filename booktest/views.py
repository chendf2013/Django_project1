from django.http import HttpResponse
from django.shortcuts import render

from django.views import View

from booktest.forms import BookForm

from django.http import HttpResponse
from django.template import loader, RequestContext


def index(request):
    """首页测试模板"""
    # # 1.获取模板
    # template = loader.get_template('../templates/index.html')
    # # 2.定义上下文
    # contex = {'city': '北京'}
    # # 3.渲染模板
    # return HttpResponse(template.render(contex))
    contex = {"city": "北京"}
    return render(request, "../templates/index.html", contex)


class Bookview(View):
    """表单测试"""

    def get(self, request):
        form = BookForm()
        return render(request, "booktest.html", {"form": form})

    def post(self, request):
        form = BookForm(request.Post)
        if form.is_valid():
            print(form.changed_data)
            return HttpResponse("ok")
        else:
            return render(request, "booktest.html", {"form": form})
