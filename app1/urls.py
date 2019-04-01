from django.contrib import admin
from django.urls import path
from .views import SchoolList, StudentList, StudentListListView, StudentDetailView, SchoolCreateView, SchoolUpdateView, SchoolDeleteView

urlpatterns = [
    path('school_list/', SchoolList.as_view(), name='school'),
    path('student_list1/', StudentList.as_view(), name='student'),
    path('student_list2/', StudentListListView.as_view(), name='student_list_view'),
    path('student_list2/<int:pk>', StudentDetailView.as_view(), name='student_detail'),
    path('create_school/', SchoolCreateView.as_view(), name='create'),
    path('update_school/<int:pk>', SchoolUpdateView.as_view(), name='update'),
    path('delete_school/<int:pk>', SchoolDeleteView.as_view(), name='delete'),
]
