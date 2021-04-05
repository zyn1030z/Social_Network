from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from core.models import Post


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home/index.html'
