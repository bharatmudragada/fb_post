class ReactionTypeParameter(object):
    @staticmethod
    def get_param_name():
        param_names = {
            "parameter_name": "ReactionTypeParameter",
            "parameter_field_name": "reaction_type"
        }
        return param_names

    @staticmethod
    def get_serializer_class():
        serializer_options = {
            "param_serializer": "ReactionTypeSerializer",
            "param_serializer_import_str": "from fb_post.build.serializers.definitions.ReactionType.ReactionTypeSerializer import ReactionTypeSerializer",
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