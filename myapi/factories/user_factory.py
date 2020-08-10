import factory
import factory.django

from ..models import MyUser, ActivityPeriod

class MyUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MyUser

    user_id = factory.Faker('pystr_format')
    real_name = factory.Faker('name')
    tz = factory.Faker('country')

class ActivityPeriodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ActivityPeriod

    user_id = factory.Iterator(MyUser.objects.all())
    start_time = factory.Faker('date_time')
    end_time = factory.Faker('date_time')
