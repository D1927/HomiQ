from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# To manage as a admin
admin.site.register(User, UserAdmin)
