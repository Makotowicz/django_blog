from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(View):

    def get(self, request):
        all_posts = Post.objects.all()
        return render(request, 'blog/home.html', {'all_posts': all_posts})


class PostDetailView(View):

    def get(self, request, pk):
        isolated_post = Post.objects.get(pk=pk)
        return render(request, 'blog/post_detail.html', {'single_post': isolated_post})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(View):

    def get(self, request, pk):
        isolated_post = Post.objects.get(pk=pk)
        return render(request, 'blog/post_detail.html', {'single_post': isolated_post})


class PostDeleteView(View):

    def get(self, request, pk):
        isolated_post = Post.objects.get(pk=pk)
        isolated_post.delete()
        return HttpResponseRedirect('/')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
