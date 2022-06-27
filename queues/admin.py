from django.contrib import admin

from .models import Queue, SongQueue

admin.site.register(Queue)
admin.site.register(SongQueue)
