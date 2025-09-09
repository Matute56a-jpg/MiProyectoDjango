from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'sender', 'recipient', 'created_at', 'read')
    list_filter = ('read', 'created_at', 'sender', 'recipient')
    search_fields = ('subject', 'body', 'sender__username', 'recipient__username')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
