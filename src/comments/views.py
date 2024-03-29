from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import  DeleteView

from .forms import CommentForm
from .models import Comment


def comment_thread(request, id):
    obj = get_object_or_404(Comment, id=id)
    initial_data = dict(content_type=obj.content_type, object_id=obj.object_id)
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
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

    context = dict(comment=obj, form=form)
    return render(request, "post/comment_thread.html", context)

class CommentDelete(DeleteView):
    model = Comment

    def get(self, request, id):
        obj = Comment.objects.get(id=id)
        parent_obj_url = obj.content_object.get_absolute_url()
        obj.delete()
        messages.success(request, "Comment successfully deleted")
        return HttpResponseRedirect(parent_obj_url)
