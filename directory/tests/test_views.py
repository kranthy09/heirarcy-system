import pytest
from urllib import response
from django.urls import reverse
from directory.models import Level, SubLevel
from directory.serializers import LevelSerializer, SubLevelSerialzer

# class GetCreatePortfolioListTest(APITestCase):
    
#     def test_get_portfolios_list(self):
#         response = self.client.get('/api/v1/portfolio-list')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
    
#     def test_get_portfolio_subportfolio_list(self):
#         response = self.client.get('/api/v1/portfolio-list')



    
#     def test_create_portfolio(self):
#         # url = reverse('potfolio-create')
#         data = {'name': 'Portfolio'}
#         response = self.client.post('/api/v1/portfolio-list', data=data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(response.data['name'], "Portfolio")

@pytest.mark.django_db
def test_list_portfolio(client):
    url = reverse('portfolio-list')
    response = client.get(url)

    levels = Level.objects.all()
    expected_data = LevelSerializer(levels, many=True).data

    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
def test_create_portfolio(client):
    url = reverse('portfolio-list')
    response = client.post(url, {'name': 'Project'})
    level = Level.objects.get(name='Project')
    levelserializer = LevelSerializer(level)
    assert response.data == levelserializer.data
    assert response.status_code == 201


@pytest.mark.django_db
def test_get_subportfolio_list(client, levels):
    url = reverse('portfolio-list')
    response = client.get(url)
    serializer = LevelSerializer(levels, many=True)
    assert response.data[0]['sublevels'] == serializer.data[0]['sublevels']

@pytest.mark.django_db
def test_get_portfolio_detail(client):
    level = Level.objects.create(name='Program')
    url = reverse('portfolio-detail', kwargs={'pk': level.id})
    response = client.get(url)
    serializer = LevelSerializer(level)
    assert response.status_code == 200
    assert response.data['name'] == 'Program'
    assert response.data == serializer.data

@pytest.mark.django_db
def test_get_subportfolio_list(client, level):
    sublevels = SubLevel.objects.create(name='SubPortfolio', parent=level)
    url = reverse('subportfolio-list')
    response = client.get(url)
    sublevels = SubLevel.objects.all()
    serializer = SubLevelSerialzer(sublevels, many=True)
    print(serializer.data)
    print(response.data)
    assert response.data == serializer.data
    assert response.data[0]['parent'] == serializer.data[0]['parent']
