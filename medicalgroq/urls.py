# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_view, name='chat_view'),
    path('chat/completion/', views.ChatCompletionView.as_view(), name='chat_completion'),
]