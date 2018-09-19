from django import forms

# class BookForm(forms.Form):
#     """普通的表单"""
#     title = forms.CharField(label="书名",required=True,max_length=50)
#     pub_date = forms.DateField(label="出版日期",required=True)
#
from booktest.models import BookInfo


class BookForm(forms.ModelForm):
    """模板表单"""

    class Meta:
        # 制定模板
        model = BookInfo
        # 向表单内添加模板内的字段
        fields = ["btitle", "bcomment", "bpub_date"]
