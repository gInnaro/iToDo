from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.home, name='note'),
    path('category/<category_id>/', views.category_detail, name='detail'),
]