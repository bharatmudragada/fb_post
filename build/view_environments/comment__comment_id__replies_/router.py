path_method_dict = {
    "comment/(?P<comment_id>\\w+)/replies/": {
        "GET": "get_replies_to_comment"
    }
}


def comment__comment_id__replies_(request, *args, **kwargs):
    from django_swagger_utils.drf_server.utils.server_gen.get_operations_dict import get_operations_dict
    operations_dict = get_operations_dict(path_method_dict, request.path)

    from django_swagger_utils.drf_server.wrappers.router_wrapper import router_wrapper
    response = router_wrapper("fb_post", "comment__comment_id__replies_", operations_dict, request, *args, **kwargs)
    return response