from django.urls import path
from . import views

urlpatterns = [

    path('get_user/', views.Get_user.as_view(), name='getuser'), # 获取所有用户  字典

]
