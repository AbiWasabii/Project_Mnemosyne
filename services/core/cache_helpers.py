from services.core.cache import get_cache
from services.core.cache import set_cache


def cached_call(key, function):

    cached = get_cache(key)

    if cached:

        return cached

    result = function()

    set_cache(
        key,
        result
    )

    return result