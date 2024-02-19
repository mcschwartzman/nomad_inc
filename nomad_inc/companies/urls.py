from django.urls import path

from . import views

app_name = "companies"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:company_id>/details/", views.detail, name="details"),
    path("<int:company_id>/profits/", views.profits, name="profits"),
    path("<int:company_id>/relocate/", views.relocate, name="relocate")
]