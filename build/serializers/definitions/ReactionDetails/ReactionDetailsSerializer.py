from fb_post.build.serializers.definitions.User.UserSerializer import UserSerializer
from fb_post.build.serializers.definitions.User.UserSerializer import UserType
from fb_post.build.serializers.definitions.ReactionType.ReactionTypeSerializer import ReactionTypeSerializer
from fb_post.build.serializers.definitions.ReactionType.ReactionTypeSerializer import ReactionTypeType

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize

class ReactionDetailsType(UserType, ReactionTypeType):
    def __init__(self, **validated_data):
        UserType.__init__(self, **validated_data)
        ReactionTypeType.__init__(self, **validated_data)
        

class ReactionDetailsSerializer(UserSerializer, ReactionTypeSerializer):
    def create(self, validated_data):
        
        userSerializer, _ = deserialize(UserSerializer, validated_data, many=False, partial=True)
        validated_data.update(userSerializer.__dict__)
        
        reactionTypeSerializer, _ = deserialize(ReactionTypeSerializer, validated_data, many=False, partial=True)
        validated_data.update(reactionTypeSerializer.__dict__)
        
        return ReactionDetailsType(**validated_data)
