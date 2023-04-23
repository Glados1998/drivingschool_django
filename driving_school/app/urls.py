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
    path('instructor-creation/', views.instructor_creation, name='instructor-creation'),
    path('instructor-edit-delete/<int:instructor_pk>/', views.instructor_edit_delete, name='instructor-edit-delete'),
    path('secretary-creation/', views.secretary_creation, name='secretary-creation'),
    path('secretary-edit-delete/<int:secretary_pk>/', views.secretary_edit_delete, name='secretary-edit-delete'),
    path('admin-creation/', views.admin_creation, name='admin-creation'),
    path('admin-edit-delete/<int:admin_pk>/', views.admin_edit_delete, name='admin-edit-delete'),
    path('student-details/<int:student_pk>/', views.student_details, name='student-details'),
    path('instructor-details/<int:instructor_pk>/', views.instructor_details, name='instructor-details'),
]
