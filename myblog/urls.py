from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='home'),
    path('blog_create/', views.blog_create_view, name='blog-create'),
    path('blog_list/', views.blog_list_view, name='blog-list'),
    path('blog_update/<int:pk>/', views.blog_update_view, name='blog-update'),
    path('blog_detail/<int:pk>/', views.blog_detail_view, name='blog-detail'),
    path('blog_delete/<int:pk>/', views.blog_delete_view, name='blog-delete'),
]
