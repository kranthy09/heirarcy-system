from rest_framework import serializers
from tree.models import Parent, Child


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = "__all__"
    
    def create(self, validated_data):
        print(validated_data)
        parent_data = validated_data.pop('parent')
        if type(parent_data) == dict():
            parent = Parent.objects.create(**parent_data)    
        else:
            parent = Parent.objects.get(pk=parent_data)
        return Child.objects.create(parent=parent.id, **validated_data)
    

class ParentSerializer(serializers.ModelSerializer):
    childs = ChildSerializer(many=True, read_only=True)
    class Meta:
        model = Parent
        fields = ["id", "name", "level", "childs"]
