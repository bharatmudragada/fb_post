from rest_framework import serializers
from fb_post.build.serializers.definitions.ReplyData.ReplyDataSerializer import ReplyDataSerializer

class GetCommentRepliesListResponseSerializer(serializers.ListSerializer):
    child = ReplyDataSerializer()
