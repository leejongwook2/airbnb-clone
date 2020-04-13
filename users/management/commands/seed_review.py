import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as review_models
from users import models as user_models
from rooms import models as room_models

class Command(BaseCommand):

    help = "This command creates reviews"

    # python manage.py loveyou --times 50 명령어는 이러했다....

    def add_arguments(self, parser):
        parser.add_argument("--times", default=2,  help="how many rooms you want to create")

    def handle(self, *args, **options):
        number = options.get("number", 100)
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        print(users.count())
        print(rooms.count())
        seeder.add_entity(
            review_models.Review,
            number,
            {
            "accuracy": lambda x: random.randint(0, 6),
            "communication": lambda x: random.randint(0, 6),
            "cleanliness": lambda x: random.randint(0, 6),
            "location": lambda x: random.randint(0, 6),
            "check_in": lambda x: random.randint(0, 6),
            "value": lambda x: random.randint(0, 6),
            "room": lambda x: random.choice(rooms),
            "user": lambda x: random.choice(users),
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} review created!"))