from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path("", views.notes, name="index"),
    path("create/",views.create,name="create"),
    path("notes/",views.notes,name="notes"),
    path("notes/<int:id>",views.list,name="list"),
    path("admin/",admin.site.urls),
]