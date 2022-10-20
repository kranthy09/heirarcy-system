from rest_framework import serializers
from tree.models import Parent, Child


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = "__all__"
    

class ParentSerializer(serializers.ModelSerializer):
    childs = ChildSerializer(many=True, read_only=True)
    class Meta:
        model = Parent
        fields = "__all__"
    
    def update(self, instance, validated_data):
        print(validated_data)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        # instance.save()
        return instance
