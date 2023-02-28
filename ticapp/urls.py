from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('post_message/', views.post_message, name='post_message'),
]
