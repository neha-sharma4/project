from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})

def list_students(request):
    students = Student.objects.all()
    return render(request, 'students_list.html', {'students': students})
