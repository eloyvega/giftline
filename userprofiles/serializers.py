from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'last_login', 'id', 'first_name', 'last_name', 'is_staff', 'date_joined', 'is_superuser',
                  'email', 'is_active')
