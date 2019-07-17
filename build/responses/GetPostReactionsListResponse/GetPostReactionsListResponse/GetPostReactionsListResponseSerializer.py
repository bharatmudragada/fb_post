from rest_framework import serializers
from fb_post.build.serializers.definitions.ReactionDetails.ReactionDetailsSerializer import ReactionDetailsSerializer

class GetPostReactionsListResponseSerializer(serializers.ListSerializer):
    child = ReactionDetailsSerializer()
