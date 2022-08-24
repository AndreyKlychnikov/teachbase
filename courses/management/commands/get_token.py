from django.core.management.base import BaseCommand
from teachbase_api import HttpClient


class Command(BaseCommand):
    help = "Загрузка данных из API Teachbase"

    def add_arguments(self, parser):
        parser.add_argument("client_id", type=str)
        parser.add_argument("client_secret", type=str)

    def handle(self, *args, **options):
        client = HttpClient(
            client_id=options["client_id"], client_secret=options["client_secret"]
        )
        client.auth()
        if not client.check_token():
            self.stdout.write(self.style.ERROR("Ошибка авторизации"))
            return
        self.stdout.write(self.style.SUCCESS("Авторизация прошла успешно"))
        self.stdout.write(self.style.SUCCESS(f"Токен: {client.access_token}"))
