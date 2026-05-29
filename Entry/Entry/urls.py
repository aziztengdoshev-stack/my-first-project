"""
URL configuration for Entry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('manage_teacher/<int:pk>/', views.manage_teacher, name='manage_teacher'),
    path('student/login/', views.login_s, name='student/login'),
    path('teacher/login/', views.login_t, name='teacher/login'),
    path('director/menu/', views.dir_menu, name='dir/menu'),
    path('teacher/menu/', views.teach_menu, name='teacher/menu'),
    path('student/menu/', views.stud_menu, name='student/menu'),
    
    path('', views.enter_rol, name='enter_rol'),
    path('director/classes/', views.classes_list, name='classes_list'),
    path('director/classes/<int:class_id>/', views.manage_class, name='manage_class'),

    path('director/teachers/', views.teachers_list, name='teachers_list'), # Список учителей
    path('director/teachers/<int:teacher_id>/', views.manage_teacher, name='manage_teacher'),

    path('logout/', views.logout_user, name='logout'),
    path('director/add-teacher/', views.add_teacher_view, name='add_teacher_url'),
    path('director/teachers/edit/<int:teacher_id>/', views.edit_teacher, name='edit_teacher'),
    path('director/teachers/delete/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),
    path('classes/', views.classes_list, name='classes_list'),
    path('classes/add/', views.add_class, name='add_class'),
    path('director/classes/<int:class_id>/add_student/', views.add_student, name='add_student'),
    path('director/classes/<int:class_id>/edit/', views.edit_class, name='edit_class'),
    path('director/classes/<int:class_id>/delete/', views.delete_class, name='delete_class'),
]
