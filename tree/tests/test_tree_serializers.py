from cmath import exp
import json
import pytest
from rest_framework.exceptions import ErrorDetail
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
            "level": 1,
            "childs": []
        }
    ]
    # use
    serializer = ParentSerializer(parents, many=True)

    # assert
    assert serializer.data == exp_data

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
def test_create_child_serializer_with_parent_id(parent, child_create_data):
    exp_data = {
        "id": 1,
        "name": "Project",
        "level": 1,
        "parent": 1
    }
    serializer = ChildSerializer(data=child_create_data)
    assert serializer.is_valid() == True
    serializer.save()
    assert serializer.data == exp_data

@pytest.mark.django_db
def test_create_child_serialier_with_parent_obj(parent, create_child_parentobj_data):
    exp_data = {
        "id": 1,
        "name": "Project",
        "level": 1,
        "parent": 1
    }
    serializer = ChildSerializer(data=create_child_parentobj_data)
    assert serializer.is_valid() == True
    serializer.save()
    assert serializer.data ==exp_data
