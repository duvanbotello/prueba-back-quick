from django.urls import path
from apps.users.api.api import api_users, getuser, api_anything

urlpatterns = [
    path('users/', api_users, name='user'),
    path('users/<int:pk>/', getuser, name='get_user'),
    path('', api_anything, {'resource': ''}),
    path('<path:resource>', api_anything)
]
