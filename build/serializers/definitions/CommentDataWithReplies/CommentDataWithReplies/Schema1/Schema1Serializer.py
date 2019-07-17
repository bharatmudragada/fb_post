from rest_framework import serializers

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_object
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_list_object
from django_swagger_utils.drf_server.fields.collection_format_field import CollectionFormatField


class Schema1Type(object):
    def __init__(self, replies_count=None, replies=None,  **kwargs):
        self.replies_count = replies_count
        self.replies = replies

    def __str__(self):
        from django_swagger_utils.drf_server.utils.server_gen.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class Schema1Serializer(serializers.Serializer):
    replies_count = serializers.IntegerField(required=False, allow_null=True)
    from fb_post.build.serializers.definitions.CommentData.CommentDataSerializer import CommentDataSerializer
    replies = CommentDataSerializer(required=False, many=True)

    def create(self, validated_data):
        from fb_post.build.serializers.definitions.CommentData.CommentDataSerializer import CommentDataSerializer
        replies_val = []
        replies_list_val = validated_data.pop("replies", [])
        for each_data in replies_list_val:
            each_obj, _ = deserialize(CommentDataSerializer, each_data, many=False, partial=True)
            replies_val.append(each_obj)
        
        return Schema1Type(replies=replies_val, **validated_data)
