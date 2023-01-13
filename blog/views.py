from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View
from .models import Post
from .forms import PostForm


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


class NewPost(View):

    form_class = PostForm
    template_name = "blog/add_post.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'new_post': form})

    def post(self, request):
        form = self.form_class(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(reverse('blog-home'))
        return render(request, self.template_name, {'new_post': form})


class PostUpdateView(View):
    form_class = PostForm
    template_name = 'blog/update_post.html'

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = self.form_class(instance=post)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = self.form_class(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('post-detail', kwargs={'pk': post.pk}))
        return render(request, self.template_name, {'form': form})


class PostDeleteView(View):

    def get(self, request, pk):
        isolated_post = Post.objects.get(pk=pk)
        isolated_post.delete()
        return HttpResponseRedirect('/')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
