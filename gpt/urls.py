from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('ans/<models>&<answer>', views.ans, name='answers')
]