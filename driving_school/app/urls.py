from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('user-panel/', views.user_panel, name='user-dashboard'),
    path('logout/', views.logout_def, name='logout'),
    path('course-creation/', views.course_creation, name='course-creation'),
    path('course-edit-delete/<int:course_pk>/', views.course_edit_delete, name='course-edit-delete'),
    path('student-creation/', views.student_creation, name='student-creation'),
    path('student-edit-delete/<int:student_pk>/', views.student_edit_delete, name='student-edit-delete'),
]
