from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task
from datetime import datetime
from django.utils.timezone import now
from base64 import b64decode
from datetime import datetime


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'