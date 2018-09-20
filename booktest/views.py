import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from booktest.forms import BookForm
from django.http import HttpResponse
from datetime import datetime
from django.template import loader, RequestContext

from booktest.models import BookInfo
from booktest.serializer import BookInfoSerializer


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

    # 在forms中定义表单类
    # 在当前文件导入表单类
    # 初始化表单类
    # 将表单类装入模板渲染

    def get(self, request):
        form = BookForm()
        return render(request, "booktest.html", {"form": form})

    def post(self, request):
        # 将获取到的表单内容传入表单类初始化表单(post大写)
        form = BookForm(request.POST)
        # 表单验证
        if form.is_valid():
            # 输出表单的纯净内容
            print(form.cleaned_data)
            return HttpResponse("ok")
        else:
            return render(request, "booktest.html", {"form": form})


class BooksRest(View):
    """书籍整体"""

    def post(self, request):
        """增加图书"""
        print("进入函数")
        # 获取内容(将字节转化为字符串)
        content = request.body.decode()
        # 将json字符串转化成字典
        content_dic = json.loads(content)
        # 获书名
        title = content_dic.get("btitle")
        # 获取出版时间,将时间格式化并且去掉时分秒
        pub_date = content_dic.get("bpub_date")
        # 将字符串时间转化为时间对象
        pub_date = datetime.strptime(pub_date, "%Y-%m-%d").date()
        # 创建图书模型病上传
        book = BookInfo.objects.create_book(title, pub_date)

        book_dict = {
            "btitle": book.btitle,
            "bcomment": book.bcomment,
            "bread": book.bread,
            "bpub_date": book.bpub_date,
            "id": book.id
        }
        return JsonResponse(book_dict, status=201)

    def get(self, request):
        """获取所有书籍"""
        books = BookInfo.objects.all()
        books_list = []
        for book in books:
            book_dict = {
                "btitle": book.btitle,
                "bcomment": book.bcomment,
                "bread": book.bread,
                "bpub_date": book.bpub_date,
                "id": book.id
            }

            books_list.append(book_dict)
        # 默认参数是字典，想要传递列表，架上后面的safe属性
        return JsonResponse(books_list, safe=False)


class BookRest(View):

    def get(self, request, pk):
        """获取单一书籍"""
        book = BookInfo.objects.get(id=pk)
        book_dict = {
            "btitle": book.btitle,
            "bcomment": book.bcomment,
            "bread": book.bread,
            "bpub_date": book.bpub_date,
            "id": book.id
        }
        return JsonResponse(book_dict)

    def delete(self, request, pk):
        """删除书籍"""
        try:
            book = BookInfo.objects.get(pk=pk)
        except Exception as ret:
            return HttpResponse("服务器查询错误")
        book.delete()
        return HttpResponse("删除书籍成功")

    def put(self, request, pk):
        """修改书籍"""
        try:
            book = BookInfo.objects.get(pk=pk)
        except Exception as ret:
            return HttpResponse("服务器查询错误")
        json_byte = request.body
        json_dic = json.loads(json_byte.decode())

        book.btitle = json_dic.get("btitle")
        book.bpub_date = datetime.strptime(json_dic.get("bpub_date"), "%Y-%m-%d").date()
        book.bcomment = json_dic.get("bcomment")
        book.bread = json_dic.get("bread")

        book.save()
        book_dict = {
            "btitle": book.btitle,
            "bcomment": book.bcomment,
            "bread": book.bread,
            "bpub_date": book.bpub_date,
            "id": book.id
        }
        return JsonResponse(book_dict)



# 执行序列化的视图函数
def serialize(request,pk):
    # 从数据库中查询出模型对象
    book = BookInfo.objects.get(pk=pk)
    # queryset = BookInfo.objects.all()

    # 初始化序列化器, 需要把模型对象传给序列化器
    # serializer = BookInfoSerializer(book, many=True)
    serializer = BookInfoSerializer(book)
    # 执行序列化
    print(serializer.data)
    return HttpResponse("序列化成功!!!%s" % serializer.data)


# 执行反序列化的视图函数
def deserialize(request):
    # 模拟客户端提交的数据
    # data = {"btitle":"上海滩", "bpub_date":None, "id": 1}
    # 初始化序列化器, 把需要反序列化的数据传入data参数中
    data_str = request.body.decode()
    data_dic = json.loads(data_str)
    serializer = BookInfoSerializer(data=data_dic)
    # 打印校验结果
    print(serializer.is_valid())
    # 如果校验失败, 打印错误信息, 如果成功, 返回{}
    print(serializer.errors)
    # 经过校验之后的干净数据, 如果校验不成功, 返回{}
    print(serializer.validated_data)
    return HttpResponse("反序列化结束!!!%s" % serializer.validated_data)
