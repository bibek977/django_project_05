from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = 'index' ),
    path("add/", views.add, name = 'add' ),
    path("read/", views.read, name = 'read' ),
    path("update/<str:id>", views.update, name = 'update' ),
    path("delete/<str:id>", views.delete, name = 'delete' ),
]
