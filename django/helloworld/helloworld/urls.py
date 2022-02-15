"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import myapp.views
#어떤 url로 요청이 들어오면 어떤 함수를 실행시킬지
urlpatterns = [
    path('admin/', admin.site.urls),
    #/home으로 url 들어오면 myapp의 views에 있는 home 함수 실행하라,
    #그리고 그 url 경로에 대한 이름을 hello world로 한다
    path('', myapp.views.home,name="hello_world"),
    path('test/', myapp.views.test,name="test"),
]
