path_method_dict = {
    "post/(?P<post_id>\\w+)/comment/(?P<comment_id>\\w+)/reply/": {
        "POST": "add_reply_to_comment"
    }
}


def post__post_id__comment__comment_id__reply_(request, *args, **kwargs):
    from django_swagger_utils.drf_server.utils.server_gen.get_operations_dict import get_operations_dict
    operations_dict = get_operations_dict(path_method_dict, request.path)

    from django_swagger_utils.drf_server.wrappers.router_wrapper import router_wrapper
    response = router_wrapper("fb_post", "post__post_id__comment__comment_id__reply_", operations_dict, request, *args, **kwargs)
    return response