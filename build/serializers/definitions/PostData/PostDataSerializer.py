from fb_post.build.serializers.definitions.PostId.PostIdSerializer import PostIdSerializer
from fb_post.build.serializers.definitions.PostId.PostIdSerializer import PostIdType
from fb_post.build.serializers.definitions.PostData.PostData.Schema1.Schema1Serializer import Schema1Serializer
from fb_post.build.serializers.definitions.PostData.PostData.Schema1.Schema1Serializer import Schema1Type
from fb_post.build.serializers.definitions.PostContent.PostContentSerializer import PostContentSerializer
from fb_post.build.serializers.definitions.PostContent.PostContentSerializer import PostContentType
from fb_post.build.serializers.definitions.PostData.PostData.Schema3.Schema3Serializer import Schema3Serializer
from fb_post.build.serializers.definitions.PostData.PostData.Schema3.Schema3Serializer import Schema3Type

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize

class PostDataType(PostIdType, Schema1Type, PostContentType, Schema3Type):
    def __init__(self, **validated_data):
        PostIdType.__init__(self, **validated_data)
        Schema1Type.__init__(self, **validated_data)
        PostContentType.__init__(self, **validated_data)
        Schema3Type.__init__(self, **validated_data)
        

class PostDataSerializer(PostIdSerializer, Schema1Serializer, PostContentSerializer, Schema3Serializer):
    def create(self, validated_data):
        
        postIdSerializer, _ = deserialize(PostIdSerializer, validated_data, many=False, partial=True)
        validated_data.update(postIdSerializer.__dict__)
        
        schema1Serializer, _ = deserialize(Schema1Serializer, validated_data, many=False, partial=True)
        validated_data.update(schema1Serializer.__dict__)
        
        postContentSerializer, _ = deserialize(PostContentSerializer, validated_data, many=False, partial=True)
        validated_data.update(postContentSerializer.__dict__)
        
        schema3Serializer, _ = deserialize(Schema3Serializer, validated_data, many=False, partial=True)
        validated_data.update(schema3Serializer.__dict__)
        
        return PostDataType(**validated_data)
