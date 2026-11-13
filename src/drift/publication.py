"""Keep local filesystem paths out of published logs and result artifacts."""
import os
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
# Do not mistake URL paths, relative paths or XML closing tags for local paths.
_PATH = re.compile(r'''(?<![\w./:<])/(?![/\s])[^\s"'`<>\[\]{},;()]+''')
_QUOTED_PATH = re.compile(r'''(["'`])(/[^\n"'`]+)\1''')
_PYTHON = re.compile(r"python(?:\d+(?:\.\d+)*)?$")


def public_text(text, root=ROOT):
    """Display paths relative to root; never change paths used to run commands."""
    if not _PATH.search(text):
        return text
    root = Path(root).resolve()
    prefix = re.compile(r'(?<![\w./:<])' + re.escape(str(root)) + r'''(/|(?=$|[\s"'`<>\[\]{},;()]))''')
    text = prefix.sub(lambda m: '' if m[1] else '.', text)

    def relative(value):
        if _PYTHON.fullmatch(Path(value).name):
            return 'python3.11'
        return os.path.relpath(value, root)

    # Quoted paths can contain spaces (including a workspace with spaces).
    text = _QUOTED_PATH.sub(lambda m: m[1] + relative(m[2]) + m[1], text)
    return _PATH.sub(lambda m: relative(m[0]), text)


def public_data(value, root=ROOT):
    """Sanitize nested string keys/values without changing measured numbers."""
    if isinstance(value, str):
        return public_text(value, root)
    if isinstance(value, dict):
        result = {}
        for key, item in value.items():
            key = public_text(key, root) if isinstance(key, str) else key
            if key in result:
                raise ValueError('Relative publication paths would collide')
            result[key] = public_data(item, root)
        return result
    if isinstance(value, (list, tuple)):
        return [public_data(item, root) for item in value]
    return value
