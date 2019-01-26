from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Post, Comment
from .forms import PostForm, CommentForm


def searchPost(request):
    if request.method == 'POST':
        try:
            q = request.POST['query']
            Posts = Post.objects.filter(title=q)
            if Posts:
                return render(request, 'post/post_list.html', {'Posts': Posts})
            else:
                try:
                    user = User.objects.get(username=q)
                    Posts = Post.objects.filter(user=user.pk)
                    return render(request, 'post/post_list.html', {'Posts': Posts})
                except User.DoesNotExist:
                    return render(request, 'post/404.html')
                return render(request, 'post/404.html')
        except KeyError:
            return render(request, 'post/404.html')


class UserProfile(DetailView):
    template_name = "post/user_profile.html"
    model = Post, User

    def get(self, request, username):
        user = User.objects.get(username=username)
        post_list = Post.objects.filter(user=user.pk)
        paginator = Paginator(post_list, 10)
        page = request.GET.get('page')

        try:
            Posts = paginator.page(page)
        except PageNotAnInteger:
            Posts = paginator.page(1)
        except EmptyPage:
            Posts = paginator.page(paginator.num_pages)

        if post_list == []:
            messages.add_message(request, messages.WARNING, "The user does not have a share!")

        context = dict(Posts=Posts, user=user)
        return render(request, self.template_name, context)


class PostList(DetailView):
    template_name = "post/post_list.html"
    model = Post

    def get(self, request):
        Posts = Post.objects.all()[::-1]
        paginator = Paginator(Posts, 5)
        page = request.GET.get('page')

        try:
            Posts = paginator.page(page)
        except PageNotAnInteger:
            Posts = paginator.page(1)
        except EmptyPage:
            Posts = paginator.page(paginator.num_pages)

        context = {'Posts': Posts}
        return render(request, self.template_name, context)


class PostDetail(DetailView):
    template_name = "post/post_detail.html"

    def get(self, request, pk):
        queryset = Post.objects.get(pk=pk)
        context = dict(post=queryset)
        return render(request, self.template_name, context)


class PostDelete(DeleteView):
    model = Post

    def get(self, request, pk):
        post = Post.objects.get(pk=pk).delete()
        messages.add_message(request, messages.SUCCESS, "Your post has been deleted!")
        return redirect("post:list")


class PostEdit(UpdateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('post:detail', args=(self.object.id, ))


class NewPost(CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.user = self.request.user.profile
        form.save()
        return redirect('post:list')


class CommentView(CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('post:detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        form.instance.userPost = Post.objects.get(pk=self.kwargs['pk'])
        form.save()
        return super(CommentView, self).form_valid(form)
