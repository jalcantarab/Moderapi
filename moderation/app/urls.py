from django.urls import path
from . import views

urlpatterns = [
    path('', views.moderation_view, name='moderation_view'),
    path('moderation-api/', views.moderation_api, name='moderation_api'),
]