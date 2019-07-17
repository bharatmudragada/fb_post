class GetReactionMetricsResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '[{"reaction_type": "LOVE", "count": 1}]',
            "response_serializer": "GetReactionMetricsResponseSerializer",
            "response_serializer_import_str": "from fb_post.build.responses.GetReactionMetricsResponse.GetReactionMetricsResponse.GetReactionMetricsResponseSerializer import GetReactionMetricsResponseSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass