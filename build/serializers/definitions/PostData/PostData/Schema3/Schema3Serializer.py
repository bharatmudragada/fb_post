from rest_framework import serializers

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_object
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_list_object
from django_swagger_utils.drf_server.fields.collection_format_field import CollectionFormatField


class Schema3Type(object):
    def __init__(self, reactions=None, comments=None, comments_count=None,  **kwargs):
        self.reactions = reactions
        self.comments = comments
        self.comments_count = comments_count

    def __str__(self):
        from django_swagger_utils.drf_server.utils.server_gen.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class Schema3Serializer(serializers.Serializer):
    from fb_post.build.serializers.definitions.ReactionsData.ReactionsDataSerializer import ReactionsDataSerializer
    reactions = ReactionsDataSerializer(required=False, allow_null=True)
    from fb_post.build.serializers.definitions.CommentDataWithReplies.CommentDataWithRepliesSerializer import CommentDataWithRepliesSerializer
    comments = CommentDataWithRepliesSerializer(required=False, many=True)
    comments_count = serializers.IntegerField(required=False, allow_null=True)

    def create(self, validated_data):
        from fb_post.build.serializers.definitions.ReactionsData.ReactionsDataSerializer import ReactionsDataSerializer
        reactions_val, _ = deserialize(ReactionsDataSerializer, validated_data.pop("reactions", None), many=False, partial=True)
        
        from fb_post.build.serializers.definitions.CommentDataWithReplies.CommentDataWithRepliesSerializer import CommentDataWithRepliesSerializer
        comments_val = []
        comments_list_val = validated_data.pop("comments", [])
        for each_data in comments_list_val:
            each_obj, _ = deserialize(CommentDataWithRepliesSerializer, each_data, many=False, partial=True)
            comments_val.append(each_obj)
        
        return Schema3Type(reactions=reactions_val, comments=comments_val, **validated_data)
