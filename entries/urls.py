from django.urls import path

from .views import client_add
from .views import client_delete
from .views import client_edit
from .views import clients_list
from .views import entries_list
from .views import entry_delete
from .views import entry_details
from .views import entry_save
from .views import home

app_name = "entries"

urlpatterns = [
    path("home/", home, name="home"),
    path("clients/", clients_list, name="clients"),
    path("clients/edit/<int:client_id>", client_edit, name="client_edit"),
    path("clients/edit/add/", client_add, name="client_add"),
    path("clients/edit/delete/<int:client_id>", client_delete, name="client_delete"),
    path("entries/", entries_list, name="entries"),
    path("entries/filter/<int:month>", entries_list, name="entries_filter"),
    path("entries/<int:entry_id>", entry_details, name="entry_details"),
    path("entries/save/<int:entry_id>", entry_save, name="entry_save"),
    path("entries/delete/<int:entry_id>", entry_delete, name="entry_delete"),
]
