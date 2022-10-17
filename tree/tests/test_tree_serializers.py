from typing import Tuple
from unicodedata import name
import pytest
from tree.models import Parent, Child
from tree.serializers import ParentSerializer, ChildSerializer

@pytest.mark.django_db
def test_parent_serializer():
    data = {
        "name": "Portfolio",
        "level": 0,
        "childs": []
    }
    serializer = ParentSerializer(data=data)
    assert serializer.is_valid() == True
    serializer.save()
    assert serializer.errors == {}
    parent = Parent.objects.get(pk=1)
    assert serializer.data['name'] == parent.name
    assert serializer.data['level'] == parent.level

@pytest.mark.django_db
def test_parent_serializer_create_method():
    data = {
        "name": "Portfolio 1",
        "level": 0,
        "childs": [
            {
                "name": "Sub Portfolio 1",
                "level": 1,
            }
        ]
    }
    serializer = ParentSerializer(data=data)

    assert serializer.is_valid() == True
    assert serializer.errors == {}
    serializer.save()
    parent = Parent.objects.get(pk=1)
    child = Child.objects.get(pk=1)
    print(Parent.objects.all())
    print(Child.objects.all())
    assert serializer.data['name'] == parent.name
    assert serializer.data['level'] == parent.level
    assert serializer.data['childs'][0]['name'] == child.name
    assert serializer.data['childs'][0]['level'] == child.level


@pytest.mark.django_db
def test_child_serializer(parent):
    data = {
        "name": "Sub Portfolio",
        "level": 1,
        "parent": 1
    }
    serializer = ChildSerializer(data=data)
    assert serializer.is_valid() == True
    assert serializer.data['name'] == "Sub Portfolio"
