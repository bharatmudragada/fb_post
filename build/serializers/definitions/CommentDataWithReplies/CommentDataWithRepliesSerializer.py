from fb_post.build.serializers.definitions.CommentData.CommentDataSerializer import CommentDataSerializer
from fb_post.build.serializers.definitions.CommentData.CommentDataSerializer import CommentDataType
from fb_post.build.serializers.definitions.CommentDataWithReplies.CommentDataWithReplies.Schema1.Schema1Serializer import Schema1Serializer
from fb_post.build.serializers.definitions.CommentDataWithReplies.CommentDataWithReplies.Schema1.Schema1Serializer import Schema1Type

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize

class CommentDataWithRepliesType(CommentDataType, Schema1Type):
    def __init__(self, **validated_data):
        CommentDataType.__init__(self, **validated_data)
        Schema1Type.__init__(self, **validated_data)
        

class CommentDataWithRepliesSerializer(CommentDataSerializer, Schema1Serializer):
    def create(self, validated_data):
        
        commentDataSerializer, _ = deserialize(CommentDataSerializer, validated_data, many=False, partial=True)
        validated_data.update(commentDataSerializer.__dict__)
        
        schema1Serializer, _ = deserialize(Schema1Serializer, validated_data, many=False, partial=True)
        validated_data.update(schema1Serializer.__dict__)
        
        return CommentDataWithRepliesType(**validated_data)
