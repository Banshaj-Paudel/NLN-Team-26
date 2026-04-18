import re

from django.utils.html import escape, strip_tags

_SCRIPT_RE = re.compile(r"(?is)<script.*?>.*?</script>")


def sanitize_text(value, *, max_length: int | None = None) -> str:
    text = "" if value is None else str(value)
    text = _SCRIPT_RE.sub("", text)
    text = strip_tags(text)
    text = str(escape(text)).strip()
    if max_length is not None:
        text = text[:max_length]
    return text


def sanitize_text_list(values, *, max_items: int = 10, item_max_length: int | None = None) -> list[str]:
    if not isinstance(values, (list, tuple)):
        return []
    cleaned: list[str] = []
    for value in values[:max_items]:
        sanitized = sanitize_text(value, max_length=item_max_length)
        if sanitized:
            cleaned.append(sanitized)
    return cleaned
