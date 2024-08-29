from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from core.models import Subject

class Command(BaseCommand):
    help = "Add a New Subject"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str,help="Name of the new Subject")
        #parser.add_argument("description", type=str,help="Description")

    def handle(self, *args, **kwargs):
        name = kwargs["name"]
        #description = kwargs["description"]
        if Subject.objects.filter(name=name).exists():
            self.stdout.write(self.style.ERROR("Subject already exists"))
        else:
            subject = Subject.objects.create(name=name)
            subject.save()
            self.stdout.write(self.style.SUCCESS("Subject added Succesfully!"))