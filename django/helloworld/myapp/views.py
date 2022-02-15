from django.shortcuts import render

# Create your views here.
# 어떠한 요청이 들어오면
def home(request):
    #요청과 함께 html을 보여줘라
    return render(request,'index.html')

def test(request):
    #요청과 함께 html을 보여줘라
    return render(request,'test.html')