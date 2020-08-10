import datetime
import random

from django.core.management.base import BaseCommand

from myapi.factories.user_factory import MyUserFactory, ActivityPeriodFactory

class Command(BaseCommand):
    help = 'Populates the database.'

    def add_arguments(self, parser):
        parser.add_argument('--myuser',
            default=2,
            type=int,
            help='The number of fake users to create.')

        parser.add_argument('--num_activity',
            default=10,
            type=int,
            help='The number of activity records to create.')

    def handle(self, *args, **options):
        for _ in range(options['myuser']):
            MyUserFactory.create()

        for _ in range(options['num_activity']):
            ActivityPeriodFactory.create()

