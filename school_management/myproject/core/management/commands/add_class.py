from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from core.models import Class

class Command(BaseCommand):
    help = "Add a New Teacher"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name of the class')
        parser.add_argument('year', type=int, help='Year of the class')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        year = kwargs['year']

        if Class.objects.filter(name=name, year=year).exists():
            self.stdout.write(self.style.ERROR("Class already exists"))
        else:    
            teacher = Class.objects.create(name=name, year=year)
            teacher.save()
            self.stdout.write(self.style.SUCCESS('Class added successfully'))