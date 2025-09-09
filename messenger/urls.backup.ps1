from django.urls import path
from . import views

urlpatterns = [
    path('redactar/<int:reply_to_id>/', views.compose, name='messenger_reply'),
    path('', views.inbox, name='messenger_inbox'),
    path('enviados/', views.sent, name='messenger_sent'),
    path('redactar/', views.compose, name='messenger_compose'),
    path('<int:pk>/', views.detail, name='messenger_detail'),
]


