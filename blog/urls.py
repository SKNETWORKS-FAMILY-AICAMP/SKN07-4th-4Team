from django.urls import path
from . import views

urlpatterns = [
    # path('<int:pk>/', views.post_page),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.index),
    # 
    path('write_page/', views.write_page),
    path('write_file/', views.write_file, name="write_file"),
    path('write_post/', views.write_post, name="write_post")
]