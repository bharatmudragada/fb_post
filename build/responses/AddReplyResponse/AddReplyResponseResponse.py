class AddReplyResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"reply_comment_id": 1}',
            "response_serializer": "ReplyCommentIdSerializer",
            "response_serializer_import_str": "from fb_post.build.serializers.definitions.ReplyCommentId.ReplyCommentIdSerializer import ReplyCommentIdSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass