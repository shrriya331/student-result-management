from django.shortcuts import render, redirect
from .forms import MarksForm
from django.contrib.auth.decorators import login_required, user_passes_test

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

