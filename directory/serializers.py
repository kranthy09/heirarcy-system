from pkgutil import read_code
from attr import field
from directory.models import Level
from rest_framework import serializers
from directory.models import Level, SubLevel

class SubLevelSerialzer(serializers.ModelSerializer):

    class Meta:
        model = SubLevel
        fields = "__all__"

class LevelSerializer(serializers.ModelSerializer):
    sublevels = SubLevelSerialzer(many=True, read_only=True)
    class Meta:
        model = Level
        fields = "__all__"