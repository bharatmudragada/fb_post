class PostParameter(object):
    @staticmethod
    def get_param_name():
        param_names = {
            "parameter_name": "CreateNewPostParameter",
            "parameter_field_name": "Post"
        }
        return param_names

    @staticmethod
    def get_serializer_class():
        serializer_options = {
            "param_serializer": "PostContentSerializer",
            "param_serializer_import_str": "from fb_post.build.serializers.definitions.PostContent.PostContentSerializer import PostContentSerializer",
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