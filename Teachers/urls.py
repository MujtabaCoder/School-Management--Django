
from django.urls import path
from .views import TeacherCls


teacher_obj = TeacherCls()


urlpatterns = [
    path('add-teacher', teacher_obj.addteacher,name='add-teacehr'),
    path('teacher_form', teacher_obj.teacher_form, name='teacher_form'),
    path('add_teacher_data_page', teacher_obj.teacher_data_page,name='add_teacher_data_page'),
    path("edit-teacher_page",teacher_obj.edit_teacher_page,name="edit-teacher"),
    path("update_teacher",teacher_obj.update_teacher,name="update_teacher"),
    path("teacher_profile",teacher_obj.teacher_profile,name="teacher_profile"),

]