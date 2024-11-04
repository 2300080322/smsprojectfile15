from django.urls import path,include
from.import views
from  django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render
from django import forms
urlpatterns=[
    path('',views.projecthomepage,name='projecthomepage'),
    #path('projectstudentpage/',views.projectstudentpage,name='studentpage'),
    path('printpagecall/',views.printpagecall,name='printpagecall'),
    path('printpagelogic/',views.printpagelogic,name='printpagelogic'),
    path('exceptionpagecall/',views.exceptionpagecall,name='exceptionpagecall'),
    path('exceptionpagelogic/',views.exceptionpagelogic,name='exceptionpagelogic'),
    path('randompagecall/',views.randompagecall,name='randompagecall'),
    path('randomlogic/',views.randomlogic,name='randomlogic'),
    path('calculatorpagecall/',views.calculatorpagecall,name='calculatorpagecall'),
    path('calculatorlogic/',views.calculatorlogic,name='calculatorlogic'),
    path('datetimepagecall/',views.datetimepagecall,name='datetimepagecall'),
    path('datetimelogic/',views.datetimelogic,name='datetimelogic'),
    path('add_task/',views.add_task,name='add_task'),
    path('<int:pk>/delete/',views.delete_task,name='delete_task'),
    path('UserRegisterPageCall/', views.UserRegisterPageCall, name='UserRegisterPageCall'),
    path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('UserLoginPageCall/',views.UserLoginPageCall,name='UserLoginPageCall'),
    path('UserLoginLogic/',views.UserLoginLogic,name='UserLoginLogic'),
    path('UserLoginLogic/',views.UserLoginLogic,name='UserLoginLogic'),
    path('logout/', views.logout, name='logout'),
    path('add_student/',views.add_student,name='add_student'),
    path('student_list/',views.student_list,name='student_list'),
    path('upload_file/',views.upload_file,name='upload_file'),

]


