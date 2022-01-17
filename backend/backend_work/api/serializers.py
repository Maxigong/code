from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from xml.etree.ElementInclude import include
from rest_framework import serializers

from ..models import ImgModel, FormModel, PostModel, AuthorModel, CommentsModel


class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgModel
        fields = '__all__'


class FormModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormModel
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField(source='post.slug')

    class Meta:
        model = CommentsModel
        # fields = '__all__'
        fields = ("id",
                  "name",
                  "title",
                  "messege",
                  "data",
                  "slug",
                  )


class PostSerializer(serializers.ModelSerializer):
    Author = serializers.StringRelatedField()
    tag = serializers.StringRelatedField(many=True)
    comments = CommentsSerializer(many=True, read_only=True)

    class Meta:
        model = PostModel
        fields = ("id", "Author", "title",
                  "body", "slug", "description", "tag", "date", 'comments', )
