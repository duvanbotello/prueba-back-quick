from django.contrib import admin

# Register your models here.
from apps.users.models import Users

admin.site.register(Users)