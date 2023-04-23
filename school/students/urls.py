from django.urls import path
from students.views import index_page, create_name, user_name_details, delete_user_name, user_names_user_birth_create, delete_birth, user_info_create, delete_info,user_work_create, delete_work

urlpatterns = [
    path('', index_page, name='index'),
    path('students/create/', create_name, name='create_name'),
    path('students/<int:pk>/', user_name_details, name='user_name_details'),
    path('students/<int:pk>/delete/', delete_user_name, name='delete_user_name'),
    path('students/<int:pk>/user_births-create', user_names_user_birth_create, name='user_names_user_birth_create'),
    path('students/<int:pk>/delete_1', delete_birth, name='delete_birth'),
    path('students/<int:pk>/delete_2', delete_info, name='delete_info'),
    path('students/<int:pk>/delete_3', delete_work, name='delete_work'),
    path('students/<int:pk>/user_infos-create', user_info_create, name='user_info_create'),
    path('students/<int:pk>/user_works-create', user_work_create, name='user_work_create'),
]

    