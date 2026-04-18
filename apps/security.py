from html.parser import HTMLParser

from django.utils.html import escape


class _PlainTextSanitizer(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self._chunks: list[str] = []
        self._ignore_depth = 0

    @property
    def text(self) -> str:
        return "".join(self._chunks)

    def handle_starttag(self, tag: str, attrs):
        if tag.lower() in {"script", "style"}:
            self._ignore_depth += 1

    def handle_endtag(self, tag: str):
        if tag.lower() in {"script", "style"} and self._ignore_depth > 0:
            self._ignore_depth -= 1

    def handle_data(self, data: str):
        if self._ignore_depth == 0:
            self._chunks.append(data)


def sanitize_text(value, *, max_length: int | None = None) -> str:
    text = "" if value is None else str(value)
    parser = _PlainTextSanitizer()
    parser.feed(text)
    parser.close()
    text = str(escape(parser.text)).strip()
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
