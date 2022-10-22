from django.contrib import admin
from django.urls import path
from tree.views import ParentDetail, ParentList, ChildList

urlpatterns = [
    path('parent-list', ParentList.as_view(), name="parent-list"),
    path('parent-detail/<int:pk>', ParentDetail.as_view(), name="parent-detail"),
    path('child-list', ChildList.as_view(), name="child-list"),
]
