from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView, UpdateView
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Post, Comment
from .forms import PostForm, CommentForm


def PostList(request):
    Posts = Post.objects.all()[::-1]
    paginator = Paginator(Posts, 10)

    page = request.GET.get('page')
    try:
        Posts = paginator.page(page)
    except PageNotAnInteger:
        Posts = paginator.page(1)
    except EmptyPage:
        Posts = paginator.page(paginator.num_pages)

    return render(request, 'post/post_list.html', {'Posts': Posts})


def PostDetail(request, pk):
    queryset = Post.objects.get(pk=pk)
    template_name = "post/post_detail.html"
    context = dict(post=queryset)
    return render(request, template_name, context)


def PostDelete(request, pk):
    post = get_object_or_404(Post, pk=pk).delete()
    messages.add_message(request, messages.INFO, "Your post has been deleted!")
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
        return reverse_lazy('post:list')

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        form.instance.userPost = Post.objects.get(pk=self.kwargs['pk'])
        form.save()
        return super(CommentView, self).form_valid(form)
