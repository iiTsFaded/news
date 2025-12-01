# articles/views.py
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin # new
)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Article

class ArticleUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, UpdateView): # new
        model = Article
        fields = (
            "title",
            "body",
        )
        template_name = "article_edit.html"
        
        def test_func(self): # new
            obj = self.get_object()
            return obj.author == self.request.user

class ArticleDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, DeleteView): # new
        model = Article
        template_name = "article_delete.html"
        success_url = reverse_lazy("article_list")
        
        def test_func(self): # new
            obj = self.get_object()
            return obj.author == self.request.user