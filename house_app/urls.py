from django.urls import path

from house_app import views

urlpatterns = [
    path("", views.HouseView, name="home"),
    path("list/", views.HouseListView, name="House-list"),
    path("create/", views.HouseCreateView, name="House-create"),
    path("detail/<str:pk>/", views.HouseView, name="House-detail"),
    path("patch/<str:pk>/", views.HouseView, name="House-patch"),
    path("delete/<str:pk>/", views.HouseView, name="House-delete"),
]
