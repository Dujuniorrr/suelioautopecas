from django.urls import path
from . import views

urlpatterns = [
    # path("client/", include("client.urls")),
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("remove/<int:id>/", views.remove, name="remove"),
    path("edit/<int:id>/", views.edit, name="edit"),
]
