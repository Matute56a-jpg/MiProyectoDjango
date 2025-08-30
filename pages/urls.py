from django.urls import path
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

urlpatterns = [
    path('', ListView.as_view(model=Post, template_name='blog/post_list.html'), name='post_list'),
    path('<int:pk>/', DetailView.as_view(model=Post, template_name='blog/post_detail.html'), name='post_detail'),
    path('crear/', LoginRequiredMixin.as_view(CreateView.as_view(
        model=Post, fields=['titulo', 'subtitulo', 'autor', 'contenido', 'imagen'],
        template_name='blog/post_form.html', success_url='/pages/'
    )), name='post_create'),
    path('<int:pk>/editar/', LoginRequiredMixin.as_view(UpdateView.as_view(
        model=Post, fields=['titulo', 'subtitulo', 'autor', 'contenido', 'imagen'],
        template_name='blog/post_form.html', success_url='/pages/'
    )), name='post_update'),
    path('<int:pk>/borrar/', LoginRequiredMixin.as_view(DeleteView.as_view(
        model=Post, template_name='blog/post_confirm_delete.html', success_url='/pages/'
    )), name='post_delete'),
]
