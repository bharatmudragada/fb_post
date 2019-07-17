from rest_framework import serializers

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_object
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_list_object
from django_swagger_utils.drf_server.fields.collection_format_field import CollectionFormatField


class UserType(object):
    def __init__(self, name=None, user_id=None, profile_pic_url=None,  **kwargs):
        self.name = name
        self.user_id = user_id
        self.profile_pic_url = profile_pic_url

    def __str__(self):
        from django_swagger_utils.drf_server.utils.server_gen.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    user_id = serializers.IntegerField(required=False, allow_null=True)
    profile_pic_url = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return UserType(**validated_data)
