from rest_framework import serializers
from fb_post.build.serializers.definitions.ReactionMetric.ReactionMetricSerializer import ReactionMetricSerializer

class GetReactionMetricsResponseSerializer(serializers.ListSerializer):
    child = ReactionMetricSerializer()
