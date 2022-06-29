from django.contrib import admin
from django.urls import path, include

import users.views

urlpatterns = [
    path('admin/', admin.site.urls),
]
