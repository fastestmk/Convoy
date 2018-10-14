from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status

from post.models import Post
from rest.serializers import PostSerializer


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        icerik = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(icerik, **kwargs)


@csrf_exempt
def posts_api(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        posts_serializer = PostSerializer(posts, many=True)
        return JSONResponse(posts_serializer.data)


@csrf_exempt
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Oyun.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        posts_serializer = PostSerializer(post)
        return JSONResponse(posts_serializer.data)
