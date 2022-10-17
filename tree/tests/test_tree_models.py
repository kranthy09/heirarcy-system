import pytest
from tree.models import Parent, Child

@pytest.mark.django_db
def test_parent_model(create_parent):
    create_parent.save()
    db_parent = Parent.objects.get(pk=1)
    assert create_parent.name == db_parent.name
    assert create_parent.level == db_parent.level

@pytest.mark.django_db
def test_child_model():
    parent = Parent.objects.create(name="Portfolio", level=0)
    child = Child.objects.create(name='Sub Portfolio', level=1, parent=parent)
    db_child = Child.objects.get(pk=1)
    assert db_child.name == child.name
    assert db_child.parent.name == child.parent.name
    assert db_child.level == child.level