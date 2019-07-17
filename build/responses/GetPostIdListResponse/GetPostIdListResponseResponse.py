class GetPostIdListResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"post_ids": [1]}',
            "response_serializer": "GetPostIdListResponseSerializer",
            "response_serializer_import_str": "from fb_post.build.responses.GetPostIdListResponse.GetPostIdListResponse.GetPostIdListResponseSerializer import GetPostIdListResponseSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass