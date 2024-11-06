from django.conf.urls import url
from django.urls import path
from live_chat import views as chat_views

urlpatterns = [
    path("<str:room_name>/", chat_views.chatPage, name="chat-room")
]
