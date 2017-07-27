# coding:utf-8
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """数据交互"""

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """ Notice that we're using hyperlinked relations in this case, with HyperlinkedModelSerializer. You can also use primary key and various other relationships, but hyperlinking is good RESTful design."""

    class Meta:
        model = Group
        fields = ('url', 'name')