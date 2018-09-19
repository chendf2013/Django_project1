from django import forms


class BookForm(forms.Form):
    title = forms.CharField(label="书名",required=True,max_length=50)
    pub_date = forms.DateField(label="出版日期",required=True)