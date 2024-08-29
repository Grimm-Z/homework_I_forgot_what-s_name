from django.core.management.base import BaseCommand
from core.models import *


class Command(BaseCommand):
    help = 'Add an entry to the Schedule'

    def add_arguments(self, parser):
        parser.add_argument('day_of_week', type=str, help='Day of Week')
        parser.add_argument('start_time', type=str, help='Start Time')
        parser.add_argument('end_time', type=str, help='End Time')
        parser.add_argument('subject', type=int, help='ID of the Subject')
        parser.add_argument('student_class', type=int, help='ID of the Student Class')
        parser.add_argument('teacher', type=int, help='ID of the Teacher')

    def handle(self, *args, **kwargs):
        day_of_week = kwargs['day_of_week']
        start_time = kwargs['start_time']
        end_time = kwargs['end_time']
        subject_id = kwargs['subject']
        student_class_id = kwargs['student_class']
        teacher_id = kwargs['teacher']

        try:
            subject = Subject.objects.get(id=subject_id)
        except Subject.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Subject with ID {subject_id} does not exist'))
            return None

        try:
            student_class = Class.objects.get(id=student_class_id)
        except Class.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Class with ID {student_class_id} does not exist'))
            return None

        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Teacher with ID {teacher_id} does not exist'))
            return None

        if Teacher.objects.get(id=teacher_id).subject != Subject.objects.get(id=subject_id):
            self.stdout.write(self.style.ERROR('This subject does not belong to the selected teacher.'))
            return None

        if Schedule.objects.filter(
                day_of_week=day_of_week,
                start_time=start_time,
                end_time=end_time,
                student_class=student_class,
        ).exists():
            self.stdout.write(self.style.ERROR('This time slot is already taken for the selected class'))
        else:
            schedule = Schedule.objects.create(
                day_of_week=day_of_week,
                start_time=start_time,
                end_time=end_time,
                subject=subject,
                student_class=student_class,
                teacher=teacher
            )
            schedule.save()
            self.stdout.write(self.style.SUCCESS('Schedule entry successfully created.'))