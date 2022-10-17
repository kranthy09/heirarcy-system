import pytest
from tree.models import Parent, Child

@pytest.fixture(scope="module", params=[("Portfolio", 0),])
def create_parent(request):
    param = request.param
    parent = Parent(name=param[0], level=param[1])
    return parent

@pytest.fixture
def parent():
    return Parent.objects.create(name="Portfolio", level=0)