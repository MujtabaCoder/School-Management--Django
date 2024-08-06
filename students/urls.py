
from django.urls import path
from students.views import StudentCls

student_obj = StudentCls()

urlpatterns = [    
    
    path('add_student_page', student_obj.add_student_page,name='add_student_page'),
    path('add_student',student_obj. add_student, name='add_student'),
    path('add_data_page', student_obj.student_data_page,name='add_data_page'),
    path('edit_student_page',student_obj. edit_student_page, name='edit_student_page'),
    path('update_student',student_obj.update_student, name='update_student'),
    path('student_profile',student_obj.student_profile, name='student_profile'),
    path('issuebook',student_obj.issuebook_view),
    
    
]



