path_method_dict = {
    "post/create/": {
        "POST": "create_post"
    }
}


def post_create_(request, *args, **kwargs):
    from django_swagger_utils.drf_server.utils.server_gen.get_operations_dict import get_operations_dict
    operations_dict = get_operations_dict(path_method_dict, request.path)

    from django_swagger_utils.drf_server.wrappers.router_wrapper import router_wrapper
    response = router_wrapper("fb_post", "post_create_", operations_dict, request, *args, **kwargs)
    return response