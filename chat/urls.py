from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('chats/', views.ChatSessionView.as_view()),
    path('chats/<uri>/', views.ChatSessionView.as_view()), # <uri> will be sent as a agr
    path('chats/<uri>/messages/', views.ChatSessionMessageView.as_view()),
]
