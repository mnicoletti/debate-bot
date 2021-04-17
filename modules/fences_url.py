import logging
from enums import url_data

log = logging.getLogger(__name__)

def obtain_fence_url(fence_type):
    return "{0}/GameIcons/{1}Fence.png".format(url_data.BASE_URL, fence_type)