# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "get_reaction_metrics"
REQUEST_METHOD = "get"
URL_SUFFIX = "post/{post_id}/reactions/metrics/"

from .test_case_01 import TestCase01GetReactionMetricsAPITestCase

__all__ = [
    "TestCase01GetReactionMetricsAPITestCase"
]
