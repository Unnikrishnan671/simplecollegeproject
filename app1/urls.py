from unicodedata import name 
from django import views
from django.urls import include,path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('about/',views.about,name='about'),
    path('coursepage/',views.coursepage,name="coursepage"),
    path('studentpage/',views.studentpage,name="studentpage"),
    path('show/',views.show,name="show"),

    path('usercreate/',views.usercreate,name="usercreate"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('add_course/',views.add_course,name="add_course"),
    path('add_student/',views.add_student,name="add_student"),
    path('student1/',views.student1,name="student1"),
    path('course1/',views.course1,name="course1"),

    
]