from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_page),
    path('write_page/', views.write_page)
]