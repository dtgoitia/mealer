import datetime
import random
import string


def timestamp() -> str:
    return (
        datetime.datetime.now()
        .isoformat()[:-3]
        .replace("-", "_")
        .replace("T", "-")
        .replace(":", "_")
        .replace(".", "_")
    )


def hash() -> str:
    """Return a 8 digits length random string."""
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
