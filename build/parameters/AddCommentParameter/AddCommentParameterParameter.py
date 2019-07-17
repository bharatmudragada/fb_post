class CommentDetailsParameter(object):
    @staticmethod
    def get_param_name():
        param_names = {
            "parameter_name": "AddCommentParameter",
            "parameter_field_name": "comment_details"
        }
        return param_names

    @staticmethod
    def get_serializer_class():
        serializer_options = {
            "param_serializer": "CommentTextSerializer",
            "param_serializer_import_str": "from fb_post.build.serializers.definitions.CommentText.CommentTextSerializer import CommentTextSerializer",
            "param_serializer_required": False,
            "param_serializer_array": False
        }
        return serializer_options
        

    @staticmethod
    def get_serializer_field():
        pass

    @staticmethod
    def get_url_regex():
        pass