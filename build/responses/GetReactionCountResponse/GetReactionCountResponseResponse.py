class GetReactionCountResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"count": 1}',
            "response_serializer": "GetReactionCountResponseSerializer",
            "response_serializer_import_str": "from fb_post.build.responses.GetReactionCountResponse.GetReactionCountResponse.GetReactionCountResponseSerializer import GetReactionCountResponseSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass