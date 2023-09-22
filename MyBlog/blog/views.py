from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Post

# Create your views here.
class Index(ListView):
    model = Post

class Detail(DetailView):
    model = Post

class Create(CreateView):
    model = Post
    fields = ['title', 'body']
    success_url = reverse_lazy('index')

class Update(UpdateView):
    model = Post
    fields = ['title', 'body']

class Delete(DeleteView):
    model = Post