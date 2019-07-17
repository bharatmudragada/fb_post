class GetPostReactionsListResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '[{"name": "string", "user_id": 1, "profile_pic_url": "string", "reaction_type": "LOVE"}]',
            "response_serializer": "GetPostReactionsListResponseSerializer",
            "response_serializer_import_str": "from fb_post.build.responses.GetPostReactionsListResponse.GetPostReactionsListResponse.GetPostReactionsListResponseSerializer import GetPostReactionsListResponseSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass