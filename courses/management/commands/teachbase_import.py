from django.core.management.base import BaseCommand
from teachbase_api import HttpClient

from courses.serializers import CourseSerializer


class Command(BaseCommand):
    help = "Загрузка данных из API Teachbase"

    def add_arguments(self, parser):
        parser.add_argument("access_token", type=str)

    def handle(self, *args, **options):
        client = HttpClient(access_token=options["access_token"])
        self.stdout.write(self.style.SUCCESS("Загрузка данных из API Teachbase"))
        courses = client.get_courses()
        serializer = CourseSerializer(data=courses, many=True)
        serializer.is_valid()
        serializer.save()
        self.stdout.write(self.style.SUCCESS("Загрузка данных завершена"))
