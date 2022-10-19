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
        Parent(name="Sub Portfolio 2", level=1)
    ]
    return Parent.objects.bulk_create(objs)

@pytest.fixture
def child(parent):
    return Child.objects.create(name="Project", level=1, parent=parent)

@pytest.fixture
def child_create_data(parent):
    return {
            "name": "Project",
            "level": 1,
            "parent": 1
        }

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
