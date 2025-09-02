from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'fecha_creacion')
    list_filter = ('fecha_creacion',)
    search_fields = ('titulo', 'subtitulo', 'autor', 'contenido')
    ordering = ('-fecha_creacion',)
