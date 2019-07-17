path_method_dict = {
    "post/(?P<post_id>\\w+)/": {
        "GET": "get_post_details",
        "DELETE": "delete_post"
    }
}


def post__post_id__(request, *args, **kwargs):
    from django_swagger_utils.drf_server.utils.server_gen.get_operations_dict import get_operations_dict
    operations_dict = get_operations_dict(path_method_dict, request.path)

    from django_swagger_utils.drf_server.wrappers.router_wrapper import router_wrapper
    response = router_wrapper("fb_post", "post__post_id__", operations_dict, request, *args, **kwargs)
    return response