from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view


urlpatterns = [
    path("cls/", Class_Base_View.as_view()),
    path('stu/', Student_View.as_view()),
    path('delete/<int:id>/', Delete_Student.as_view()),
    path('update/<int:id>/', Update_Student.as_view()),
    path('login/', auth_view.LoginView.as_view(template_name="app/login.html")),
    path('logout/', auth_view.LogoutView.as_view(template_name="app/logout.html"))
]
