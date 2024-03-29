from rest_framework import serializers

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_object
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_list_object
from django_swagger_utils.drf_server.fields.collection_format_field import CollectionFormatField


class ReplyDataType(object):
    def __init__(self, comment_id=None, commenter=None, commented_at=None, comment_content=None,  **kwargs):
        self.comment_id = comment_id
        self.commenter = commenter
        self.commented_at = commented_at
        self.comment_content = comment_content

    def __str__(self):
        from django_swagger_utils.drf_server.utils.server_gen.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class ReplyDataSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField(required=False, allow_null=True)
    from fb_post.build.serializers.definitions.User.UserSerializer import UserSerializer
    commenter = UserSerializer(required=False, allow_null=True)
    commented_at = serializers.DateTimeField(required=False, allow_null=True, format='%Y-%m-%d %H:%M:%S')
    comment_content = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        from fb_post.build.serializers.definitions.User.UserSerializer import UserSerializer
        commenter_val, _ = deserialize(UserSerializer, validated_data.pop("commenter", None), many=False, partial=True)
        
        return ReplyDataType(commenter=commenter_val, **validated_data)
