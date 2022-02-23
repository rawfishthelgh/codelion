from django.shortcuts import render,redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm,CommentForm

# Create your views here.
def home(request):
    #블로그의 모든 객체 가져옴
    # posts = Blog.objects.all()
    #객체를 필터해서 가져옴
    #날짜 역순
    posts = Blog.objects.filter().order_by('-date')

    return render(request,'index.html',{'posts':posts})

#보여주는 함수
def new(request):
    return render(request,'new.html')
#저장하는 함수
def create(request):
    if (request.method=="POST"):
        post=Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

#django form 이용으로 입력값 받기
# get(= 입력값을 받을 수 있는 html 보여주기)
# post(= 입력한 내용을 데이터베이스에 저장 즉 form에서 입력한 내용 처리)
#  둘 다 처리 가능한 함수
def formcreate(request):
    if request.method=='POST':
        #입력내용 db에 저장
        form = BlogForm(request.POST)
        if form.is_valid():
            #유효하면 저장
            post=Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        # 입력 받을 수 있는 html 갖다주기
        form = BlogForm()
    #form을 딕셔너리 형태로 넘겨줌
    return render(request,'form_create.html',{'form':form})

def modelformcreate(request):
    if request.method=='POST' or request.method == "FILES":
        #입력내용 db에 저장
        form = BlogModelForm(request.POST,request.FILES)
        if form.is_valid():
            #유효하면 저장
            form.save()
            return redirect('home')
    else:
        # 입력 받을 수 있는 html 갖다주기
        form = BlogModelForm()
    #form을 딕셔너리 형태로 넘겨줌
    return render(request,'form_create.html',{'form':form})

# id별로 다른 페이지 띄우므로 blog_id 값까지 받아줘야 함
def detail(request,blog_id):
    #blog_id번째 블로그 글을 db에서 가져오는 코드
    #get_object_or_404는 pk값을 이용해 특정 모델의 한 객체만 가져옴
    #Blog에 해당하는 객체 중 pk값이 위에서 받은 blog_id 값인 객체 하나를 가져와라
    blog_detail=get_object_or_404(Blog,pk=blog_id)
    #comment 띄우는 코드
    comment_form=CommentForm()

    # detail.html로 띄워 주는 코드
    return render(request,'detail.html',{'blog_detail':blog_detail,'comment_form':comment_form})

def create_comment(request,blog_id):
    #post 요청으로 넘어온 form data들을 CommentForm양식에 담아서 filled_form으로 저장
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        #아직 어떤 포스트에 대한 글인지 모르지 일단 작성(commit)하지 말고 대기하라는 뜻
        finished_form=filled_form.save(commit=False)
        #Blog객체 중 id에 맞는 글을 가져와 finished_form의 post(Comment 모델의 칼럼)에 넣어줌
        finished_form.post = get_object_or_404(Blog,pk=blog_id)
        finished_form.save()
    #해당 blog_id 값을 프리픽스로 갖는 detail url로 이동
    #redirect('애칭', parameter) 해주면 google.com/1 이런식으로 뒤에 붙는 값을 지정해줄수있다.
    return redirect('detail',blog_id)