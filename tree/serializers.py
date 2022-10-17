from rest_framework import serializers
from tree.models import Parent, Child


class ChildSerializer(serializers.ModelSerializer):

    class Meta:
        model = Child
        fields = ["name", "level"]

class ParentSerializer(serializers.ModelSerializer):
    childs = ChildSerializer(many=True)
    class Meta:
        model = Parent
        fields = "__all__"
    
    def create(self, validated_data):
        childs_data = validated_data.pop('childs')
        parent = Parent.objects.create(**validated_data)
        for child_data in childs_data:
            Child.objects.create(**child_data, parent=parent)
        return parent
