from rest_framework import serializers

from .models import MyUser, ActivityPeriod

class ActivityPeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time','user_id')

class MyUserSerializer(serializers.HyperlinkedModelSerializer):
    activity = ActivityPeriodSerializer(read_only=True, many=True)
    class Meta:
        model = MyUser
        fields = ('user_id', 'real_name', 'tz', 'activity')

