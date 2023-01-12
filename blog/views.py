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
from .forms import PostForm


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def list_view(request):

    context = {}

    context["all_posts"] = Post.objects.all()

    return render(request, "blog/home.html", context)

# class PostListView(View):
#
#     def get(self, request):
#         all_posts = Post.objects.all()
#         return render(request, 'blog/home.html', {'all_posts': all_posts})


def single_post(request, pk):

    context = {}

    context["single_post"] = Post.objects.get(pk=pk)

    return render(request, "blog/post_detail.html", context)


# class PostDetailView(View):
#
#     def get(self, request, pk):
#         isolated_post = Post.objects.get(pk=pk)
#         return render(request, 'blog/post_detail.html', {'single_post': isolated_post})


def create_post(request):
    context = {}

    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "blog/add_post.html", context)


def update_post(request, pk):
    context = {}

    isolated_post = Post.objects.get(pk=pk)

    form = PostForm(request.POST or None, instance=isolated_post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/post/" + f'{pk}/')

    context["form"] = form

    return render(request, "blog/update_post.html", context)

# class PostUpdateView(View):
#
#     def get(self, request, pk):
#         isolated_post = Post.objects.get(pk=pk)
#         return render(request, 'blog/post_detail.html', {'single_post': isolated_post})


def delete_post(request, pk):

    isolated_post = Post.objects.get(pk=pk)
    isolated_post.delete()

    return HttpResponseRedirect('/')


# class PostDeleteView(View):
#
#     def get(self, request, pk):
#         isolated_post = Post.objects.get(pk=pk)
#         isolated_post.delete()
#         return HttpResponseRedirect('/')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
