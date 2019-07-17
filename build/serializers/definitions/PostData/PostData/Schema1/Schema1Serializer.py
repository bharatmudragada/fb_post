from rest_framework import serializers

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_object
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_list_object
from django_swagger_utils.drf_server.fields.collection_format_field import CollectionFormatField


class Schema1Type(object):
    def __init__(self, posted_by=None, posted_at=None,  **kwargs):
        self.posted_by = posted_by
        self.posted_at = posted_at

    def __str__(self):
        from django_swagger_utils.drf_server.utils.server_gen.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class Schema1Serializer(serializers.Serializer):
    from fb_post.build.serializers.definitions.User.UserSerializer import UserSerializer
    posted_by = UserSerializer(required=False, allow_null=True)
    posted_at = serializers.DateTimeField(required=False, allow_null=True, format='%Y-%m-%d %H:%M:%S')

    def create(self, validated_data):
        from fb_post.build.serializers.definitions.User.UserSerializer import UserSerializer
        posted_by_val, _ = deserialize(UserSerializer, validated_data.pop("posted_by", None), many=False, partial=True)
        
        return Schema1Type(posted_by=posted_by_val, **validated_data)
