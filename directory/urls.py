from django.contrib import admin
from django.urls import path
from directory.views import PortfolioList, PortfolioDetail
urlpatterns = [
    path('portfolio-list',  PortfolioList.as_view(), name='portfolio-list'),
    path('portfolio-detail/<int:pk>',  PortfolioDetail.as_view(), name='portfolio-detail'),
    # path('portfolio-create',  PortfolioCreate.as_view(), name='create-level'),
    
    # path('/sub-portfolio-create/<int:pk>',  SubPortfolioCreate.as_view()),
    # path('/sub-portfolio-list',  SubPortfolioList.as_view()),
    # path('/sub-portfolio/<int:pk>',  SubPortfolio.as_view()),
    
]
