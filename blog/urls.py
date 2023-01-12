from django.urls import path
from .views import (
    list_view,
    single_post,
    create_post,
    update_post,
    delete_post
)
from . import views

urlpatterns = [
    path('', list_view, name='blog-home'),
    path('post/<int:pk>/', single_post, name='post-detail'),
    path('post/new/', create_post, name='post-create'),
    path('post/<int:pk>/update/', update_post, name='post-update'),
    path('post/<int:pk>/delete/', delete_post, name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
