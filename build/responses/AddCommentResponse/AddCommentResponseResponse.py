class AddCommentResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"comment_id": 1}',
            "response_serializer": "CommentIdSerializer",
            "response_serializer_import_str": "from fb_post.build.serializers.definitions.CommentId.CommentIdSerializer import CommentIdSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass