class GetCommentRepliesListResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '[{"comment_id": 1, "commenter": {"name": "string", "user_id": 1, "profile_pic_url": "string"}, "commented_at": "2099-12-31 00:00:00", "comment_content": "string"}]',
            "response_serializer": "GetCommentRepliesListResponseSerializer",
            "response_serializer_import_str": "from fb_post.build.responses.GetCommentRepliesListResponse.GetCommentRepliesListResponse.GetCommentRepliesListResponseSerializer import GetCommentRepliesListResponseSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass