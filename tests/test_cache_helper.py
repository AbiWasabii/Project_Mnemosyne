from services.core.cache_helpers import cached_call


def expensive():

    print(
        "Running expensive function..."
    )

    return "hello"


print(
    cached_call(
        "test",
        expensive
    )
)

print(
    cached_call(
        "test",
        expensive
    )
)