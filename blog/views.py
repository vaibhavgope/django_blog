from django.views.generic import ListView, DetailView  # new
from .models import Post


class BlogListView(ListView):

    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):

    model = Post
    template_name = 'post_detail.html'
