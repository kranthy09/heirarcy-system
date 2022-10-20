from unicodedata import name
import pytest, json
from django.urls import reverse
from tree.models import Parent, Child
from tree.serializers import ParentSerializer, ChildSerializer

@pytest.mark.django_db
def test_get_parent_list_api_view(client, parents):
    url = reverse('parent-list')
    resp = client.get(url)
    serializer = ParentSerializer(parents, many=True)
    assert serializer.data == resp.data
    print(resp.data)
    assert resp.status_code == 200

@pytest.mark.django_db
def test_post_parent_list_api_view(client, parent_create_data):
    url = reverse('parent-list')
    resp = client.post(url, data=parent_create_data, content_type="application/json")
    parents = Parent.objects.all()
    serializer = ParentSerializer(parents, many=True)
    assert resp.data == serializer.data
    assert resp.status_code == 201

@pytest.mark.django_db
def test_get_parent_detail_api_view(client):
    parent = Parent.objects.create(name="Portfolio", level=0)
    url = reverse('parent-detail', kwargs={"pk": parent.id})
    resp = client.get(url)
    serializer = ParentSerializer(parent)
    assert resp.data == serializer.data
    assert resp.status_code == 200

@pytest.mark.django_db
def test_update_parent_detail_api_view(client):
    updated_data = {
        "name": "New Sub Portfolio",
        "level": 1
    }
    parent = Parent.objects.create(name="Sub Portfolio", level=1)
    url = reverse('parent-detail',kwargs={"pk": 1})
    resp = client.put(
        url,
        data=updated_data,
        content_type="application/json"
    )
    serializer = ParentSerializer(parent,data=updated_data)
    assert serializer.is_valid() == True
    serializer.save()
    assert serializer.data == resp.data


@pytest.mark.django_db
def test_update_name_field_parent_detail_api_view(client):
    updated_data = {
        "name": "New Sub Portfolio"
    }
    parent = Parent.objects.create(name="Sub Portfolio", level=1)
    url = reverse('parent-detail',kwargs={"pk": 1})
    resp = client.put(
        url,
        data=updated_data,
        content_type="application/json"
    )
    serializer = ParentSerializer(parent,data=updated_data, partial=True)
    assert serializer.is_valid() == True
    serializer.save()
    assert serializer.data == resp.data