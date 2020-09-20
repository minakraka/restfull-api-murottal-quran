from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Surat


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class SuratSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Surat
        fields = ['no_surat', 'nama_surat']