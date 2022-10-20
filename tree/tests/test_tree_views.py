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
