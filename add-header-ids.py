#!/usr/bin/env python3
"""Add the id anchors from an inline table of contents to the matching markdown headers.

The table of contents is expected to contain list entries of the form:

    - [Header title](#the-generated-id)

For each such entry, the matching header (any level, e.g. `## Header title`)
gets a span appended:

    ## Header title<span id="the-generated-id"></span>

Usage:

    add-header-ids.py path/to/file.md [more.md ...]
"""

import re
import sys

# Matches a TOC entry: optional indent, list marker, [title](#id)
TOC_RE = re.compile(r'^\s*[-*]\s*\[(?P<title>.+?)\]\(#(?P<id>[^)]+)\)\s*$')
# Matches a markdown ATX header, capturing the hashes and the (trimmed) text.
HEADER_RE = re.compile(r'^(?P<hashes>#{1,6})\s+(?P<text>.+?)\s*$')
# Matches a trailing span so it can be stripped before (re)matching the title.
ANCHOR_RE = re.compile(r'\s*<span id="[^"]*"> </span>\s*$')


def process(path):
    with open(path, encoding='utf-8') as f:
        lines = f.read().splitlines()

    # Build title -> id map from the TOC entries.
    title_to_id = {}
    for line in lines:
        m = TOC_RE.match(line)
        if m:
            title_to_id[m.group('title').strip()] = m.group('id')

    changed = 0
    for i, line in enumerate(lines):
        m = HEADER_RE.match(line)
        if not m:
            continue
        # Strip any existing trailing anchor so the title can be (re)matched.
        text = ANCHOR_RE.sub('', m.group('text')).strip()
        anchor_id = title_to_id.get(text)
        if anchor_id is None:
            continue
        new_line = f'{m.group("hashes")} {text}<span id="{anchor_id}"> </span>'
        if new_line != line:
            lines[i] = new_line
            changed += 1

    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')

    print(f'{path}: added {changed} header anchor(s)')


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    for path in argv[1:]:
        process(path)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
