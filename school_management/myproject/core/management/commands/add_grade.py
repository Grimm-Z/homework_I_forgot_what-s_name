from django.core.management.base import BaseCommand
from core.models import Grade, Student, Subject


class Command(BaseCommand):
    help = 'Add a Grade for Student'

    def add_arguments(self, parser):
        parser.add_argument('student', type=int, help='ID of the Student')
        parser.add_argument('subject', type=int, help='ID of the Subject')
        parser.add_argument('grade', type=int, help='Grade')
        parser.add_argument('date', type=str, help='Date')

    def handle(self, *args, **kwargs):
        student_id = kwargs['student']
        subject_id = kwargs['subject']
        grade = kwargs['grade']
        date = kwargs['date']
        print(student_id, subject_id, grade, date)
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Student with ID {student_id} does not exist'))
            return None

        try:
            subject = Subject.objects.get(id=subject_id)
        except Subject.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Subject with ID {subject_id} does not exist'))
            return None

        if Grade.objects.filter(student=student, subject=subject, date=date).exists():
            self.stdout.write(self.style.ERROR('Grade already exists for this student, subject, and date'))
        else:
            Grade.objects.create(grade=grade, student=student, subject=subject, date=date)
            self.stdout.write(self.style.SUCCESS(f'Grade {grade} for student {student} in subject {subject} on {date} has been processed successfully.'))