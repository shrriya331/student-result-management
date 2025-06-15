from django.db import models
from django.contrib.auth.models import User

# 1. Student model
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.roll_no}"

# 2. Subject model
class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

# 3. Marks model
class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.FloatField()
    max_marks = models.FloatField(default=100)

    class Meta:
        unique_together = ('student', 'subject')

    def __str__(self):
        return f"{self.student.roll_no} - {self.subject.code}: {self.marks_obtained}/{self.max_marks}"
