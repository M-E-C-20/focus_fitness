from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog, BlogComment, BlogView, Like
from .forms import BlogPostForm


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, **kwargs):
        """Counts the number of authenticated users view the blog """
        object = super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            BlogView.objects.get_or_create(user=self.request.user, blog=object)
        return object


class BlogCreateView(CreateView):
    form_class = BlogPostForm
    model = Blog
    success_url = '/blog/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context


class BlogUpdateView(UpdateView):
    form_class = BlogPostForm
    model = Blog
    success_url = '/blog/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        })
        return context


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = '/blog/'


def like(request, slug):
    """ Checks to see if the use has liked the blog
    If True, then delete the like if False then create the like"""
    blog = get_object_or_404(Blog, slug=slug)
    like_qs = Like.objects.filter(user=request.user, blog=blog)
    if like_qs.exists():
        # unlike the post
        like_qs[0].delete()
        return redirect('blog:details', slug=slug)
    Like.objects.create(user=request.user, blog=blog)
    return redirect('blog:details', slug=slug)
