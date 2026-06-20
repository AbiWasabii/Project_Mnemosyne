from services.core.cache import get_cache
from services.core.cache import set_cache


set_cache(
    "Alex_identity",
    "Alex is a devoted boyfriend."
)

print(
    get_cache(
        "Alex_identity"
    )
)