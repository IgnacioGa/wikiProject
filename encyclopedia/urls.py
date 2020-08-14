from django.urls import path

from . import views

app_name = "ency"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.page, name="page"),
    path("search", views.search, name="search"),
    path("Rpage", views.Rpage, name="Rpage"),
    path("create", views.create, name="create"),
    path("edit/<str:entry>", views.edit, name="edit")
]
