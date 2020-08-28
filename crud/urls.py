from django.urls import path
from .import views

urlpatterns = [
    path('', views.create_user, name='create'),
    path('update/<int:id>', views.update_user, name='update'),
    path('delete/<int:id>', views.delete_user, name='delete'),
]
