from django.urls import path
from . import views

urlpatterns = [
    path("", views.transfer_key, name="transfer_key"),
]
