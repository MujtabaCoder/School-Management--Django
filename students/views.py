
from django.shortcuts import render, redirect
from .models import Student
from Administration.models import Library
from django.contrib import messages
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from datetime import date, timedelta
# from . import forms,models
from .forms import IssuedBookForm




class StudentCls():
    

    def add_student(self,request):
        if request.method == 'POST':    
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            gender = request.POST.get('gender')
            date_of_birth = request.POST.get('date_of_birth')
            roll = request.POST.get('roll')
            blood_group = request.POST.get('blood_group')
            religion = request.POST.get('religion')
            email = request.POST.get('email')
            student_class_id = request.POST.get('student_class_id')
            section = request.POST.get('section')
            admission_id = request.POST.get('admission_id')
            phone = request.POST.get('phone')
            photo = request.FILES.get('photo')

            
            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                date_of_birth=date_of_birth,
                roll=roll,
                blood_group=blood_group,
                religion=religion,
                email=email,
                studentclass_id=student_class_id,
                section=section,
                admission_id=admission_id,
                phone=phone,
                photo=photo
            )
            return redirect('add_data_page')
            # return render(request, 'add-student.html')
            # messages.success(request, 'Student added successfully!')
            # return redirect('students')  # Redirect to the student list page or any other page

        return render(request, 'add-student.html')  # Render the form page
  
    def base(self,request):
        return render(request,"base.html")
    
    def add_student_page(self,request):
        request.session["url"] = request.path
        if request.session.get("username") is not None:
            return render(request,"add-student.html")
        else:
            return HttpResponseRedirect("login")
        
    def student_data_page(self,request):
        request.session["url"] = request.path
        if request.session.get("username") is not None:
            students = Student.objects.all()
            return render(request, 'students.html', {'students': students})
        
        else:
            return HttpResponseRedirect("login")
    
    def edit_student_page(self,request):
        request.session["url"] = request.path
        if request.session.get("username") is not None:
            student_id = request.GET.get('student_id')
            student = Student.objects.get(id=student_id) 
            return render(request, 'edit-student.html', {'student': student})
        else:
            return HttpResponseRedirect("login")
    
    def update_student(self,request):
        if request.method == 'POST':
            student_id = request.POST.get('student_id')             
            Student.objects.filter(id=student_id).update(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                gender=request.POST.get('gender'),
                date_of_birth=request.POST.get('date_of_birth'),
                roll=request.POST.get('roll'),
                blood_group=request.POST.get('blood_group'),
                religion=request.POST.get('religion'),
                email=request.POST.get('email'),
                student_class_id=request.POST.get('student_class_id'),
                section=request.POST.get('section'),
                admission_id=request.POST.get('admission_id'),
                phone=request.POST.get('phone'),
                
            )

            return render(request, 'students.html')
            # return JsonResponse({"status":"1","message":"Student data updated  successfully!"}) 
    def student_profile(self,request):
        request.session["url"] = request.path
        if request.session.get("username") is not None:
            student_id = request.GET.get('student_id')
            student = Student.objects.get(id=student_id) 
            return render(request, 'student-details.html', {'student': student})
        else:
            return HttpResponseRedirect("login")
        
    

    def student_borrowed_books(self,request, student_id):
        try:
            student = Student.objects.get(id=student_id)
            borrowed_books = Student.objects.filter(student=student)

            # Calculate penalties for overdue books (assuming a 14-day borrowing period)
            today = date.today()
            for borrowed_book in borrowed_books:
                if borrowed_book.return_date < today:
                    overdue_days = (today - borrowed_book.return_date).days
                    penalty = overdue_days * 5  # Assuming a penalty of 5 units per day
                    borrowed_book.penalty = penalty
                    borrowed_book.save()

            return render(request, 'student_borrowed_books.html', {'student': student, 'borrowed_books': borrowed_books})
        except Student.DoesNotExist:
            return HttpResponse("Student not found.")
        
    


    def issuebook_view(self,request):
        form = IssuedBookForm(request.POST or None)

        if request.method == 'POST' and form.is_valid():
            form.save()  # This will create an instance of IssuedBook with the form data
            return render(request, 'bookissued.html')

        return render(request, 'issuebook.html', {'form': form})

    # def viewissuedbookbystudent(self,request):
    #     student=models.Student.objects.filter(user_id=request.user.id)
    #     issuedbook=models.IssuedBook.objects.filter(enrollment=student[0].enrollment)

    #     li1=[]

    #     li2=[]
    #     for ib in issuedbook:
    #         books=models.Book.objects.filter(isbn=ib.isbn)
    #         for book in books:
    #             t=(request.user,student[0].enrollment,student[0].branch,book.name,book.author)
    #             li1.append(t)
    #         issdate=str(ib.issuedate.day)+'-'+str(ib.issuedate.month)+'-'+str(ib.issuedate.year)
    #         expdate=str(ib.expirydate.day)+'-'+str(ib.expirydate.month)+'-'+str(ib.expirydate.year)
    #         #fine calculation
    #         days=(date.today()-ib.issuedate)
    #         print(date.today())
    #         d=days.days
    #         fine=0
    #         if d>15:
    #             day=d-15
    #             fine=day*10
    #         t=(issdate,expdate,fine)
    #         li2.append(t)

    #     return render(request,'library/viewissuedbookbystudent.html',{'li1':li1,'li2':li2})
        
    
        
    
    

    


# Create your views here.

