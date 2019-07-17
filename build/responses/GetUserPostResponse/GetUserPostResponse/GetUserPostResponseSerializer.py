from rest_framework import serializers
from fb_post.build.serializers.definitions.PostData.PostDataSerializer import PostDataSerializer

class GetUserPostResponseSerializer(serializers.ListSerializer):
    child = PostDataSerializer()
