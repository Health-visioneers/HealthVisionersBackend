from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ChatMessage

class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'content', 'timestamp')
    search_fields = ('user__username', 'content',)

admin.site.register(ChatMessage, ChatMessageAdmin)