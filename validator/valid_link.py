import re


def valid_link(link: str) -> bool:
    pattern = re.compile(r"^(https?://)?([a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+)(/.*)?$")
    return bool(pattern.match(link))
