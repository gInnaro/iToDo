from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.Category_views.home, name='home'),
    path('note', views.Category_views.note, name='note'),
    path('login/', views.logins, name='logins'),
    path("signup/", views.RegisterUser.as_view(), name="signup"),
    path('category', views.Category_views.category_info, name='category'),
    path('category/<int:category_id>/', views.Note_views.note_info, name='detail'),
    path('category/edit_<int:category_id>/', views.Category_views.edit_category, name='edit_category'),
    path('category/<int:category_id>/delete_<int:note_id>/', views.Note_views.delete_note, name='note_delete'),
    path('category/create', views.Category_views.create_category, name='create_category'),
    path('category/delete/<int:category_id>', views.Category_views.delete_category, name='delete_category'),
    path('category/delete_<int:note_id>/', views.Note_views.delete_note, name='note_delete'),
    path('note/create', views.Note_views.create_note, name='create_note'),
    path('note/<note_id>', views.Note_views.note_detail, name='note_detail'),
]