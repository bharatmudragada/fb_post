from django_swagger_utils.drf_server.decorators.request_response import request_response
from django_swagger_utils.drf_server.default.parser_mapping import PARSER_MAPPING
from django_swagger_utils.drf_server.default.renderer_mapping import RENDERER_MAPPING
from fb_post.build.responses.GetPostIdListResponse.GetPostIdListResponse.GetPostIdListResponseSerializer import GetPostIdListResponseSerializer


options = {
    'METHOD': 'GET',
    'REQUEST_WRAPPING_REQUIRED': False,
    'REQUEST_ENCRYPTION_REQUIRED': False,
    'REQUEST_IS_PARTIAL': False,
    'PARSER_CLASSES': [
        PARSER_MAPPING["application/json"]
    ],
    'RENDERER_CLASSES': [
        RENDERER_MAPPING["application/json"]
    ],
    'REQUEST_QUERY_PARAMS_SERIALIZER': None,
    'REQUEST_HEADERS_SERIALIZER': None,
    'REQUEST_SERIALIZER': None,
    'REQUEST_SERIALIZER_MANY_ITEMS': False,
    'RESPONSE': {
        
        '201' : {
           'RESPONSE_SERIALIZER': GetPostIdListResponseSerializer,
           'RESPONSE_SERIALIZER_MANY_ITEMS':  False,
           'HEADERS_SERIALIZER': None,
        }
        
    },
    "SECURITY":{

        "oauth" : [
            "read"
            
        ]
    }
}

app_name = "fb_post"
operation_id  = "get_positive_posts"
group_name = ""

@request_response(options=options, app_name=app_name, operation_id=operation_id, group_name=group_name)
def get_positive_posts(request, *args, **kwargs):
    args = (request,) + args
    from django_swagger_utils.drf_server.wrappers.view_env_wrapper import view_env_wrapper
    return view_env_wrapper(app_name, "get_positive_posts", group_name, *args, **kwargs)
