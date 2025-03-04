from django.urls import path
from . import views
app_name = 'search'
urlpatterns = [
    path('', views.search_page),
    path('write_page/', views.write_page),
    path('write_file/', views.write_file, name="write_file"),
    path('write_post/', views.write_post, name="write_post")
]