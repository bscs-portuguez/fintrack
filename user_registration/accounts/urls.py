from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', views.logout_view, name='logout'),
    path('encode/', views.encode, name='encode'),
    path('', views.index, name='index'),
    path('update/<int:row_id>/', views.update_row, name='update_row'),
]
