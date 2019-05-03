from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    user = serializers.CharField()
    title = serializers.CharField()
    content = serializers.CharField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
