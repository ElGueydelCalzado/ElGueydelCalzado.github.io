from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addsku/", views.addSKU, name="addSKU"),
    path("<str:sku>", views.searchSKU, name="searchSKU")   
]