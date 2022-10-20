import json
from unicodedata import name
import pytest
from rest_framework.exceptions import ErrorDetail
from rest_framework.response import Response
from tree.models import Parent, Child
from tree.serializers import ParentSerializer, ChildSerializer

@pytest.mark.django_db
def test_parent_serializer_get_single_parent(parent):
    # define
    exp_data = {
        "id": 1,
        "name": "Portfolio",
        "level": 0,
        "childs":[]
    }
    # use
    serializer = ParentSerializer(parent)

    # assert
    assert serializer.data == exp_data

@pytest.mark.django_db
def test_parent_serializer_get_parent_list(parents):
    # define
    exp_data = [
        {
            "id": 1,
            "name": "Portfolio 1",
            "level": 0,
            "childs": []
        },
        {
            "id": 2,
            "name": "Sub Portfolio 2",
            "level": 0,
            "childs": []
        }
    ]
    # use
    serializer = ParentSerializer(parents, many=True)

    # assert
    output_data = json.loads(json.dumps(serializer.data))
    assert output_data == exp_data

@pytest.mark.django_db
def test_create_parent_serializer():
    data = {
        "name": "Portfolio",
        "level": 1
    }
    exp_data = {
        "id": 1,
        "name": "Portfolio",
        "level": 1,
        "childs": []
    }
    serializer = ParentSerializer(data=data)
    assert serializer.is_valid() == True
    serializer.save()
    print(serializer.data)  
    assert serializer.data == exp_data

@pytest.mark.django_db
def test_create_multiple_parent_serializer():
    data = [
        {
            "name": "Portfolio 1",
            "level": 0
        },
        {
            "name": "Sub Portfolio 1",
            "level": 1
        }
    ]
    exp_data = [
        {
            "id": 1,
            "name": "Portfolio 1",
            "level": 0,
            "childs": []
        },
        {
            "id": 2,
            "name": "Sub Portfolio 1",
            "level": 1,
            "childs": []
        }
    ]
    serializer = ParentSerializer(data=data, many=True)
    assert serializer.is_valid() == True
    serializer.save()
    print(serializer.errors)
    assert serializer.errors == []
    print(serializer.data)
    assert serializer.data == exp_data

@pytest.mark.django_db
def test_in_valid_level_field_create_parent_serializer():
    exp_data = {'level': [ErrorDetail(string='A valid integer is required.', code='invalid')]}
    
    in_valid_data = {
        "name": "Portfolio",
        "level": "p"
    }
    serializer = ParentSerializer(data=in_valid_data)
    assert serializer.is_valid() == False
    print(serializer.errors)
    assert serializer.errors == exp_data

@pytest.mark.django_db
def test_get_single_child_serializer(child):
    exp_data = {
        "id": 1,
        "name": "Project",
        "level": 1,
        "parent": 1
    }
    serializer = ChildSerializer(child)
    assert serializer.data == exp_data

@pytest.mark.django_db
def test_create_child_serializer_with_parent_id(child_create_data):
    parent_obj = Parent.objects.create(name="portfolio", level=0)
    exp_data = {
        "id": 1,
        "name": "Project",
        "level": 1,
        "parent": parent_obj.id
    }
    print(child_create_data)
    serializer = ChildSerializer(data=child_create_data)
    assert serializer.is_valid() == True
    serializer.save()
    assert serializer.data == exp_data

@pytest.mark.django_db
def test_create_child_serialier_with_invalid_parent_field(create_child_parentobj_data):
    exp_data = {'parent': [ErrorDetail(string='Incorrect type. Expected pk value, received dict.', code='incorrect_type')]}
    serializer = ChildSerializer(data=create_child_parentobj_data)
    assert serializer.is_valid() == False
    assert serializer.errors == exp_data

@pytest.mark.django_db
def test_get_list_child_serializer(childs):
    exp_data = [
        {
            'id': 1,
            "name": "Project 1",
            "level": 1,
            "parent": 1
        },
        {
            "id": 2,
            "name": "Project 2",
            "level": 1,
            "parent": 2
        }
    ]
    print(childs)
    serializer = ChildSerializer(childs, many=True)
    output_data = json.loads(json.dumps(serializer.data))
    print(output_data)
    assert output_data == exp_data

@pytest.mark.django_db
def test_partial_update_parent_serializre(parent):
    data = {
        "name": "New Portfolio"
    }
    exp_data = {
        "id": 1,
        "name": "New Portfolio",
        "level": 0,
        "childs": []
    }
    serializer = ParentSerializer(parent, data=data, partial=True)
    assert serializer.is_valid() == True
    print(serializer.errors)
    serializer.save()
    assert serializer.data == exp_data

@pytest.mark.django_db
def test_update_child_serializer(parents):
    exp_data = {
        "id": 1,
        "name": "Sub Portfolio 1",
        "level": 1,
        "parent": 2
    }
    child = Child.objects.create(name="Sub Portfolio", level=1, parent=parents[0])
    new_data = {
        "name": "Sub Portfolio 1",
        "level": 1,
        "parent": 2
    }
    serializer = ChildSerializer(child, data=new_data)
    assert serializer.is_valid() == True
    serializer.save()
    assert serializer.data == exp_data
    assert serializer.data['name'] == "Sub Portfolio 1"

