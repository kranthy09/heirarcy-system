import pytest
from tree.models import Parent, Child


@pytest.fixture
def parent():
    parent = Parent.objects.create(name="Portfolio", level=0)
    return parent

@pytest.fixture
def parents():
    objs = [
        Parent(name="Portfolio 1", level=0),
        Parent(name="Sub Portfolio 2", level=0)
    ]
    return Parent.objects.bulk_create(objs)

@pytest.fixture
def child(parent):
    return Child.objects.create(name="Project", level=1, parent=parent)

@pytest.fixture
def childs(parents):
    objs = [
        Child(name="Project 1",level=1, parent=parents[0]),
        Child(name="Project 2",level=1, parent=parents[1]),
    ]
    return Child.objects.bulk_create(objs)

@pytest.fixture
def child_create_data():
    return {
            "name": "Project",
            "level": 1,
            "parent": 1
        }
@pytest.fixture
def list_child_create_data():
    return [
        {
            "name": "Project 1",
            "level": 1,
            "parent": 1
        },
        {
            "name": "Project 2",
            "level": 1,
            "parent": 2
        }
    ]

@pytest.fixture
def create_child_parentobj_data():
    return {
            "name": "Project",
            "level": 1,
            "parent": {
                "name": "Sub Portfolio",
                "level": 0
            }
        }

@pytest.fixture
def parent_create_data():
    return [
        {
            "name": "Portfolio 1",
            "level": 0
        },
        {
            "name": "Sub Portfolio 1",
            "level": 1
        }
    ]