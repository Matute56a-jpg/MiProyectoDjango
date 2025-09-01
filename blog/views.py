from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-fecha_creacion"]

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["titulo", "subtitulo", "autor", "contenido", "imagen"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["titulo", "subtitulo", "autor", "contenido", "imagen"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")
