from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView

from comments.forms import CommentForm
from comments.models import Comment

from .forms import PostForm
from .models import Post


def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    initial_data = dict(
        content_type=instance.get_content_type, object_id=instance.id
    )
    form = CommentForm(request.POST or None, initial=initial_data)

    if form.is_valid():
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        parent_obj = None

        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()

        new_comment = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_data,
            parent=parent_obj,
        )
        return redirect(new_comment.content_object.get_absolute_url())

    comments = instance.comments
    context = dict(
        title=instance.title, instance=instance, comments=comments, comment_form=form
    )
    return render(request, "post/post_detail.html", context)


class PostCreate(CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class PostUpdate(View):
    form_class = PostForm
    template_name = "post/post_form.html"

    def get(self, request, slug):
        instance = get_object_or_404(Post, slug=slug)
        form = self.form_class(request.POST or None, instance=instance)
        context = dict(
            title = instance.title, instance = instance, form = form
        )
        return render(request, self.template_name, context)

    def post(self, request, slug):
        instance = get_object_or_404(Post, slug=slug)
        form = self.form_class(request.POST or None, instance=instance)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect(instance.get_absolute_url())
        return render(request, self.template_name, context)


class PostList(DetailView):
    template_name = "post/post_list.html"
    model = Post

    def get(self, request):
        queryset_list = Post.objects.all()
        query = request.GET.get("q")

        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)
                | Q(content__icontains=query)
                | Q(user__first_name__icontains=query)
                | Q(user__last_name__icontains=query)
            ).distinct()

        paginator = Paginator(queryset_list, 8)
        page_request_var = "page"
        page = request.GET.get(page_request_var)

        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        context = dict(
            object_list = queryset,
            page_request_var = page_request_var
        )

        return render(request, self.template_name, context)


class PostDelete(DeleteView):
    model = Post

    def get(self, request, slug):
        instance = get_object_or_404(Post, slug=slug)
        instance.delete()
        messages.success(request, "Successfully deleted")
        return redirect("posts:list")


class UserProfile(DetailView):
    template_name = "post/user_profile.html"
    model = Post, User

    def get(self, request, username):
        user = User.objects.get(username=username)
        post_list = Post.objects.filter(user=user.pk)
        paginator = Paginator(post_list, 10)
        page = request.GET.get("page")

        try:
            Posts = paginator.page(page)
        except PageNotAnInteger:
            Posts = paginator.page(1)
        except EmptyPage:
            Posts = paginator.page(paginator.num_pages)

        if post_list == []:
            messages.add_message(
                request, messages.WARNING, "The user does not have a share!"
            )

        context = dict(Posts=Posts, user=user)
        return render(request, self.template_name, context)
