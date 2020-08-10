from rest_framework import viewsets

from .serializers import MyUserSerializer, ActivityPeriodSerializer
from .models import MyUser, ActivityPeriod


class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

class ActivityPeriodViewSet(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer
