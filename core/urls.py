from django.urls import path
from django.contrib.auth import views as auth_views

from core.views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
]
