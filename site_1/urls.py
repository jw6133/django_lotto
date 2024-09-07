from django.contrib import admin
from django.urls import path
from lotto import views

urlpatterns = [
 path('admin/', admin.site.urls),
 # path('', views.index),
 path('hello/', views.hello, name='hello_main'), # lotto > views.py 파일의 hello 함수 호출
 path('lotto/', views.index, name='index'), # lotto > views.py 파일의 index 함수 호출
 path('lotto/new', views.post, name = "new_lotto"),
 # lottokey는 detail() 함수의 parameter name
 path('lotto/<int:lottokey>/detail', views.detail, name='detail'),
]
