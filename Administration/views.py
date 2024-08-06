from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import SchoolClass,Library
from .models import User_Login
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404


class AdministrationCls():
    def login_page(self,request):
            return render(request,"login.html")
    def base(self,request):
        return render(request,"base.html")
    def add_class_page(self,request):
        request.session["url"] = request.path
        if request.session.get("username") is not None:
            return render(request,"add-class.html")
        else:
            return HttpResponseRedirect("login")
    
    # Create your views here.
    
    def create_class(self,request):
        if request.method == 'POST':
            student_class = request.POST.get('student_class')
            fees = request.POST.get('fees')

            # Validate and process the form data as needed
            if student_class and fees:
                try:
                    # Convert to appropriate data types if needed
                    student_class = int(student_class)
                    fees = float(fees)

                    # Check if a SchoolClass with the same student_class already exists
                    if SchoolClass.objects.filter(student_class=student_class).exists():
                        # Handle case where the class already exists
                        return HttpResponse("Class already exists. Please choose a different class.")

                    # Create SchoolClass instance
                    SchoolClass.objects.create(student_class=student_class, fees=fees)

                    # Redirect to a success page or do additional processing
                    return redirect('class_data_page')
                except (ValueError, TypeError):
                    # Handle invalid data or conversion errors
                    pass

        return render(request, 'add-class.html')

    
    def class_data_page(self,request):
            student_class = SchoolClass.objects.all()
            print("-------------------",student_class)
            return render(request, 'class-list.html', {'student_class': student_class})
    
    def update_class(self,request):
        if request.method == 'POST':
            student_class = request.POST.get('student_class')
            fees = request.POST.get('fees')

            # Validate and process the form data as needed
            if student_class and fees:
                try:
                    # Convert to appropriate data types if needed
                    student_class = int(student_class)
                    fees = float(fees)

                    # Check if a SchoolClass with the given student_class exists
                    school_class = SchoolClass.objects.get(student_class=student_class)

                    # Update the fees for the existing SchoolClass instance
                    school_class.fees = fees
                    school_class.save()

                    # Redirect to a success page or do additional processing
                    return redirect('class_data_page')
                except (ValueError, TypeError, SchoolClass.DoesNotExist):
                    # Handle invalid data, conversion errors, or if the class doesn't exist
                    pass

        return render(request, 'update-class.html')  # Create a template for the update form
    
    def edit_class_page(self,request):
            student_class_id = request.GET.get('SchoolClass_id')
            student_class = SchoolClass.objects.get(id=student_class_id) 
            return render(request,'edit-class.html', {'student_classes': student_class})
    
    def register_page(self,request):
        return render(request,"register.html")
    
    
    def register_user(self,request):
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            role = request.POST['role']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']

            # Validate password match
            if password != confirm_password:
                raise ValidationError("Passwords do not match")

            # Create user profile
            User_Login.objects.create(
                username=username,
                email=email, 
                role=role,
                password=password
            )
            

            return HttpResponseRedirect('login')  # Use the correct URL pattern
  # Redirect to login page after successful registration

        return render(request, 'register.html')

    def login_page(self,request):
        return render(request,"login.html")
    
    def not_found(self,request):
        return render(request,"404.html")
    
    def user_login(self, request):
        if request.method == "POST":
            username = request.POST.get("username", "").strip()
            password = request.POST.get("password", "").strip()
            if username and password:
                try:
                    fetchUser = User_Login.objects.get(username=username, password=password)
                    if fetchUser.username == username and fetchUser.password == password:
                        request.session["username"] = fetchUser.username
                        request.session["password"] = fetchUser.password
                        request.session["role"] = fetchUser.role

                        if fetchUser.role == "Teacher":
                            if request.session.get("url") is not None:
                                return HttpResponseRedirect(request.session["url"])
                            else:
                                return HttpResponseRedirect("teacher-list")
                        else:
                            if request.session.get("url") is not None:
                                return HttpResponseRedirect(request.session["url"])
                            else:
                                return HttpResponseRedirect("student-list")
                except User_Login.DoesNotExist:
                    return HttpResponseRedirect("not_found")
            else:
                return JsonResponse({"success": "0", "message": "One or more data is not given or invalid"})
        else:
            return JsonResponse({"success": "0", "message": "Only POST request is allowed"})


            
    def user_log_out(self,request):
        if request.session.get("username") is not None:
            del request.session["username"]
            del request.session["password"]
            del request.session["role"]
            return HttpResponseRedirect("login")
        else:
            return HttpResponseRedirect("login")
        
    def add_book(self,request):
        if request.method == 'POST':
            book_name = request.POST.get('book_name')
            language = request.POST.get('language')
            department = request.POST.get('department')
            student_class_id = request.POST.get('student_class')
            status = request.POST.get('status')
            book_quantity = request.POST.get('book_quantity')
            if not book_name:
                return HttpResponse("Book name cannot be empty.")
            elif not book_quantity:
                 return HttpResponse("book_quantity cannot be empty.")
            try:
                student_class = SchoolClass.objects.get(id=student_class_id)
            except SchoolClass.DoesNotExist:
                return HttpResponse("SchoolClass does not exist.")

            Library.objects.create(
                book_name=book_name,
                language=language,
                department=department,
                student_class=student_class,
                status=status,
                book_quantity=book_quantity
            )

            return HttpResponseRedirect('book_list_page')  # Redirect to the book list page

        school_classes = SchoolClass.objects.all()
        return render(request, 'add-book.html', {'school_classes': school_classes})

    def edit_book(self,request):
        if request.method == 'POST':
            book_id = request.POST.get('book_id') 
            Library.objects.filter(id=book_id).update(
                book_quantity = request.POST.get('new_quantity')
            )
            return redirect ( 'book_list_page')


    def add_book_page(self,request):
        request.session["url"] = request.path
        if request.session.get("username") is not None:
            return render(request,"add-book.html")
        else:
            return HttpResponseRedirect("login")
        
    def book_list_page(self,request):
        request.session["url"] = request.path
        if request.session.get("username") is not None:
            books = Library.objects.all()
            return render(request, 'book-list.html', {'books': books})
        
        else:
            return HttpResponseRedirect("login")
    
    def edit_book_page(self,request):
        request.session["url"] = request.path
        if request.session.get("username") is not None:
            book_id = request.GET.get('book_id')
            book = Library.objects.get(id=book_id) 
            return render(request, 'edit-book.html', {'book': book})
        else:
            return HttpResponseRedirect("login")
        
        

# Create your views here.
