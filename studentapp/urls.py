from django.urls import path, include
from . import views
app_name= 'studentapp'
urlpatterns = [
    path('projectStudentpage/', views.projectStudentpage, name='projectStudentpage'),
    path('view_marks/', views.view_marks, name='view_marks'),

]