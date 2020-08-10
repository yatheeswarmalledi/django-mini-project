from django.contrib import admin
from .models import MyUser, ActivityPeriod

# Register your models here.
admin.site.register(MyUser)
admin.site.register(ActivityPeriod)
