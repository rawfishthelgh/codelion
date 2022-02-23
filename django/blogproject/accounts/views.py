from django.shortcuts import render,redirect
from django.contrib import auth
# Create your views here.
def login(request):
    #POST 요청은 로그인 처림
    if request.method == "POST":
        userid = request.POST['username']
        pwd = request.POST['password']
        #받아온 유저의 네임과 패스워드가 실제로 장고에 등록되어 있는지 확인하는 메소드
        user = auth.authenticate(request, username=userid, password=pwd)
        #유저가 실제로 있다면
        if user is not None:
            #로그인 수행
            auth.login(request,user)
            return redirect('home')
        #유저가 없으면 로그인 탭으로 돌아감
        else:
            return render(request,'login.html')
    #GET요청은 login form 담은 html 띄워줌
    else:
        return render(request,'login.html')

def logout(request):
    #요청을 보낸 사람을 로그아웃시켜라
    auth.logout(request)
    return redirect('home')