from django.shortcuts import render, redirect
from .forms import MarksForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Marks, Student
from django.shortcuts import get_object_or_404

def home(request):
    role = None

    if request.user.is_authenticated:
        if request.user.is_superuser:
            role = 'admin'
        elif request.user.is_staff:
            role = 'teacher'
        else:
            role = 'student'

    return render(request, 'students/home.html', {'role': role})


def is_teacher(user):
    return user.is_staff  # Or define your own logic later

@login_required
@user_passes_test(is_teacher)
def add_marks(request):
    if request.method == 'POST':
        form = MarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_marks')  # Reloads the page after submission
    else:
        form = MarksForm()
    return render(request, 'students/add_marks.html', {'form': form})

@login_required
def view_results(request):
    try:
        student = get_object_or_404(Student, user=request.user)
        results = Marks.objects.filter(student=student)
        return render(request, 'students/my_results.html', {'results': results, 'student': student})
    except:
        return render(request, 'students/my_results.html', {'error': "You are not registered as a student."})
        