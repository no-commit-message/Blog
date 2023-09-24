from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Post
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Index(LoginRequiredMixin, ListView):
    model = Post

class Detail(LoginRequiredMixin, DetailView):
    model = Post

class Create(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']
    success_url = reverse_lazy('index')

class Update(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'body']

class Delete(LoginRequiredMixin, DeleteView):
    model = Post

def top(request):
    return render(request, 'blog/top.html')