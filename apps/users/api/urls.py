from django.urls import path
from apps.users.api.api import api_users, getuser, api_anything, api_users_create, edit_user, delete_user, edit_p_user, \
    login

urlpatterns = [
    path('users/', api_users, name='user'),
    path('login', login, name='login'),
    path('users/create', api_users_create, name='api_users_create'),
    path('users/<int:pk>', getuser, name='get_user'),
    path('users/edit/<int:pk>', edit_user, name='edit_user'),
    path('users/editp/<int:pk>', edit_p_user, name='edit_p_user'),
    path('users/delete/<int:pk>', delete_user, name='delete_user'),
    path('', api_anything, {'resource': ''}),
    path('<path:resource>', api_anything)
]
