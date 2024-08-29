from django.db import models
from django.utils import timezone


# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Class(models.Model):
    name = models.CharField(max_length=100, unique=True)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Schedule(models.Model):
    DAY_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
    ]
    day_of_week = models.CharField(max_length=100, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.day_of_week} - {self.start_time} - {self.end_time} - {self.subject}'


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject')
    grade = models.PositiveIntegerField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.student} - {self.subject} - {self.grade}'