from django import forms
from .models import Blog,Comment

class BlogForm(forms.Form):
    #내가 입력하려는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class BlogModelForm(forms.ModelForm):
    class Meta:
        #어떤 모델 입력받을 것인지
        model = Blog
        #모델의 어떤 칼럼을 입력받을 것인지
        #이러면 모두 입력받는다는 의미
        fields = '__all__'
        #특정 칼럼 입력받으려면 리스트 형식으로

class CommentForm(forms.ModelForm):
    class Meta:
        #어떤 모델 입력받을 것인지
        model = Comment
        #모델의 어떤 칼럼을 입력받을 것인지
        #이러면 모두 입력받는다는 의미
        # fields = '__all__'
        fields = ['comment']