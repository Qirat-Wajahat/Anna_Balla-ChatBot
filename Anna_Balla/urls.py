from django.contrib import admin
from django.urls import path
from Anna_Balla import views

urlpatterns = [
    path("", views.home, name='home'),  # Root URL
    path("chat", views.chat, name='chat'),  # 'chat' URL
]
