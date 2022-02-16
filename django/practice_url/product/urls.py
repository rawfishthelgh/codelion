from django.urls import path, include
from product import views

urlpatterns = [
    #아무것도 입력 안한다=='products/'를 입력한 것과 같다
    path('', views.productlist),
    path('first/', views.productfirst),
]