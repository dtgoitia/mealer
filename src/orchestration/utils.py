import datetime


def timestamp() -> str:
    return (
        datetime.datetime.now()
        .isoformat()[:-3]
        .replace("-", "_")
        .replace("T", "-")
        .replace(":", "_")
        .replace(".", "_")
    )
