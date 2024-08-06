from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from .models import *
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import status # HTTP status

# Create your views here.

class TeacherCls():
    
    def teacher_form (self,request):
        request.session["url"] = request.path
        if request.session.get("username") is not None:
            return render(request,"add-teacher.html")
        else:
            return HttpResponseRedirect("login")
    

    def addteacher(self,request):
        if request.method == 'POST':
            # Retrieve form data from POST request
            teacher_id = request.POST.get('teacher_id')
            name = request.POST.get('name')
            gender = request.POST.get('gender')
            date_of_birth = request.POST.get('date_of_birth')
            mobile = request.POST.get('mobile')
            joining_date = request.POST.get('joining_date')
            qualification = request.POST.get('qualification')
            experience = request.POST.get('experience')
            address = request.POST.get('address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            zip_code = request.POST.get('zip_code')
            country = request.POST.get('country')
            student_class_id=request.POST.get('student_class_id')

            # Create a new Teacher object
            teacher = Teacher(
                teacher_id=teacher_id,
                name=name,
                gender=gender,
                date_of_birth=date_of_birth,
                mobile=mobile,
                joining_date=joining_date,
                qualification=qualification,
                experience=experience,
                address=address,
                city=city,
                state=state,
                zip_code=zip_code,
                country=country,
                student_class_id=student_class_id,
            )

            # Save the object to the database
            teacher.save()

            return HttpResponse(f'Teacher {name} created successfully!')

        return render(request, 'teacher_form.html')
    
    def teacher_data_page(self,request):
        request.session["url"] = request.path
        if request.session.get("username") is not None:
            teachers = Teacher.objects.all()
            return render(request, 'teachersli.html', {'teachers': teachers})
        else:
            return HttpResponseRedirect("login")
        
    def edit_teacher_page(self,request):
        request.session["url"] = request.path
        if request.session.get("username") is not None:
            teacher_id = request.GET.get('teacher_id')
            teacher = Teacher.objects.get(id=teacher_id) 
            return render(request, 'edit-teacher.html', {'teacher': teacher})
        else:
            return HttpResponseRedirect("login")
    
    def update_teacher(self,request):
        if request.method == 'POST':
            teacherd_id = request.POST.get('teacherd_id')             
            Teacher.objects.filter(id=teacherd_id).update(
                teacher_id=request.POST.get('teacher_id'),
                name=request.POST.get('name'),
                gender=request.POST.get('gender'),
                date_of_birth=request.POST.get('date_of_birth'),
                mobile=request.POST.get('mobile'),
                joining_date=request.POST.get('joining_date'),
                qualification=request.POST.get('qualification'),
                experience=request.POST.get('experience'),
                address=request.POST.get('address'),
                city=request.POST.get('city'),
                state=request.POST.get('state'),
                zip_code=request.POST.get('zip_code'),
                country=request.POST.get('country'),
                
            )

            return render(request, 'success.html')
        
    def teacher_profile(self,request):
        request.session["url"] = request.path
        if request.session.get("username") is not None:
            teacher_id = request.GET.get('teacher_id')
            teacher = Teacher.objects.get(id=teacher_id) 
            return render(request, 'teacher-details.html', {'teacher': teacher})
        else:
            return HttpResponseRedirect("login")
        
        

# Create your views here.
