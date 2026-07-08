from django.urls import path
from rest_framework import routers
from . import views

urlpatterns =[
    path("menu-items/", views.MenuItemsView.as_view(), name="menu-item-list"),
    path("menu-items/<int:pk>/", views.SingleMenuItemView.as_view(), name="menu-item-detail"),
]