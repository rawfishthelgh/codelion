from django.urls import path, include
from board import views

urlpatterns = [
    #아무것도 입력 안한다=='boards/'를 입력한 것과 같다
    path('', views.board),
    path('first/', views.boardfirst),
]
