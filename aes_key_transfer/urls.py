from django.urls import path
from . import views

urlpatterns = [
    path("transfer-key/", views.transfer_key, name="transfer_key"),
]
