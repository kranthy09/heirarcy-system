import pytest
from directory.models import Level


@pytest.fixture
def api_client():
   from rest_framework.test import APIClient
   return APIClient()


@pytest.fixture
def root_level():
    level = Level.objects.create(name="Root Node")
    return level

@pytest.fixture
def levels():
   level1 = Level.objects.create(name="SubPortfolio")
   level2 = Level.objects.create(name='Project')
   return Level.objects.all()

@pytest.fixture
def level():
   return Level.objects.create(name="Program")
