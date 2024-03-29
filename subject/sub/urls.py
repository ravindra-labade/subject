from django.urls import path
from .views import add_subject, show_subject, update_subject, delete_subject


urlpatterns = [
    path('add/', add_subject, name='add_url'),
    path('show/', show_subject, name='show_url'),
    path('update/<int:pk>/', update_subject, name='update_url'),
    path('delete/<int:pk>/', delete_subject, name='delete_url'),
]
