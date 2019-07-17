from fb_post.build.serializers.definitions.ReactionType.ReactionTypeSerializer import ReactionTypeSerializer
from fb_post.build.serializers.definitions.ReactionType.ReactionTypeSerializer import ReactionTypeType
from fb_post.build.serializers.definitions.ReactionMetric.ReactionMetric.Schema1.Schema1Serializer import Schema1Serializer
from fb_post.build.serializers.definitions.ReactionMetric.ReactionMetric.Schema1.Schema1Serializer import Schema1Type

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize

class ReactionMetricType(ReactionTypeType, Schema1Type):
    def __init__(self, **validated_data):
        ReactionTypeType.__init__(self, **validated_data)
        Schema1Type.__init__(self, **validated_data)
        

class ReactionMetricSerializer(ReactionTypeSerializer, Schema1Serializer):
    def create(self, validated_data):
        
        reactionTypeSerializer, _ = deserialize(ReactionTypeSerializer, validated_data, many=False, partial=True)
        validated_data.update(reactionTypeSerializer.__dict__)
        
        schema1Serializer, _ = deserialize(Schema1Serializer, validated_data, many=False, partial=True)
        validated_data.update(schema1Serializer.__dict__)
        
        return ReactionMetricType(**validated_data)
