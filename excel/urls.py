from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('dashboard', views.dashboard, name="dashboard"),
    path('upload', views.upload, name="upload" ),
    path('edit/', views.edit(), name="edit" ),
    path('create/', views.create, name="create" ),
]
