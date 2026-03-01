
from django.shortcuts import render, redirect
from .models import Student

def dashboard(request):
    if request.method == "POST":
        Student.objects.create(
            first_name=request.POST['fname'],
            last_name=request.POST['lname'],
            email=request.POST['email'],
            gpa=request.POST['gpa']
        )
        return redirect('/')
    
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students': students})

def delete_student(request, id):
    Student.objects.get(id=id).delete()
    return redirect('/')
