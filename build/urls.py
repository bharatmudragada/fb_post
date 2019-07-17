from django.conf.urls import url

from fb_post.build.view_environments.post_create_.router import post_create_
from fb_post.build.view_environments.post__post_id__.router import post__post_id__
from fb_post.build.view_environments.post__post_id__reaction_.router import post__post_id__reaction_
from fb_post.build.view_environments.post__post_id__comment_.router import post__post_id__comment_
from fb_post.build.view_environments.post__post_id__comment__comment_id__reply_.router import post__post_id__comment__comment_id__reply_
from fb_post.build.view_environments.post__post_id__comment__comment_id__reaction_.router import post__post_id__comment__comment_id__reaction_
from fb_post.build.view_environments.posts_user_.router import posts_user_
from fb_post.build.view_environments.posts_reactions_positive_.router import posts_reactions_positive_
from fb_post.build.view_environments.posts_user_reacted_.router import posts_user_reacted_
from fb_post.build.view_environments.post__post_id__reactions_.router import post__post_id__reactions_
from fb_post.build.view_environments.post__post_id__reactions_metrics_.router import post__post_id__reactions_metrics_
from fb_post.build.view_environments.reactions_total_count_.router import reactions_total_count_
from fb_post.build.view_environments.comment__comment_id__replies_.router import comment__comment_id__replies_


urlpatterns = [
    url(r'^post/create/$', post_create_),
    url(r'^post/(?P<post_id>\w+)/$', post__post_id__),
    url(r'^post/(?P<post_id>\w+)/reaction/$', post__post_id__reaction_),
    url(r'^post/(?P<post_id>\w+)/comment/$', post__post_id__comment_),
    url(r'^post/(?P<post_id>\w+)/comment/(?P<comment_id>\w+)/reply/$', post__post_id__comment__comment_id__reply_),
    url(r'^post/(?P<post_id>\w+)/comment/(?P<comment_id>\w+)/reaction/$', post__post_id__comment__comment_id__reaction_),
    url(r'^posts/user/$', posts_user_),
    url(r'^posts/reactions/positive/$', posts_reactions_positive_),
    url(r'^posts/user/reacted/$', posts_user_reacted_),
    url(r'^post/(?P<post_id>\w+)/reactions/$', post__post_id__reactions_),
    url(r'^post/(?P<post_id>\w+)/reactions/metrics/$', post__post_id__reactions_metrics_),
    url(r'^reactions/total_count/$', reactions_total_count_),
    url(r'^comment/(?P<comment_id>\w+)/replies/$', comment__comment_id__replies_),
]
