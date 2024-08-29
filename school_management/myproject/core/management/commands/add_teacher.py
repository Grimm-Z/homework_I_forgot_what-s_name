from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from core.models import Teacher, Subject

class Command(BaseCommand):
    help = "Add a New Teacher"

    def add_arguments(self, parser):
        parser.add_argument('first_name', type=str, help='First Name of new Teacher')
        parser.add_argument('last_name', type=str, help='Last Name of new Teacher')
        parser.add_argument('subject', type=int, help='ID of the Subject')

    def handle(self, *args, **kwargs):
        first_name = kwargs['first_name']
        last_name = kwargs['last_name']
        subject_id = kwargs['subject']

        try: 
            subject = Subject.objects.get(id=subject_id)
        except Subject.DoesNotExist:
            self.stdout.write(self.style.ERROR("Subject with this ID doesn't exist!"))
            return None
        if Teacher.objects.filter(first_name=first_name,last_name=last_name,subject=subject).exists():
            self.stdout.write(self.style.ERROR("Teacher already exists"))
        else:    
            teacher = Teacher.objects.create(first_name=first_name, last_name=last_name, subject=subject)
            teacher.save()
            self.stdout.write(self.style.SUCCESS('Teacher added successfully'))