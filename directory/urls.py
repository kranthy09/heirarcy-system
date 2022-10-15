from django.contrib import admin
from django.urls import path
from directory.views import PortfolioList, PortfolioDetail, SubPortfolioList
urlpatterns = [
    path('portfolio-list',  PortfolioList.as_view(), name='portfolio-list'),
    path('portfolio-detail/<int:pk>',  PortfolioDetail.as_view(), name='portfolio-detail'),
    path('subportfolio-list',  SubPortfolioList.as_view(), name='subportfolio-list'),
    # path('/subportfolio-detail/<int:pk>',  SubPortfolio.as_view(), name='subportfolio-detail'),
    
]
