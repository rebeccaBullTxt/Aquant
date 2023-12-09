import re


def format_filename(filename, replace=' '):
    return re.sub(re.compile(
        '[/\\\:*?"<>|]')
        , replace,
        filename
    )
