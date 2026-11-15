"""Parse a MySQL dump of a WordPress database and extract content to JSON.

Usage: python parse_wp_dump.py <path-to-dump.sql> <out.json>
Only reads INSERT INTO statements for wp_* tables (no SQL execution).
"""
import json
import re
import sys


def parse_values(s, i):
    """Parse one '(...)' tuple starting at s[i] == '('. Returns (list, next_index)."""
    assert s[i] == "("
    i += 1
    row = []
    while True:
        while s[i] in " \n\r\t":
            i += 1
        c = s[i]
        if c == "'":
            i += 1
            buf = []
            while True:
                ch = s[i]
                if ch == "\\":
                    nxt = s[i + 1]
                    buf.append({"n": "\n", "r": "\r", "t": "\t", "0": "\0", "Z": "\x1a"}.get(nxt, nxt))
                    i += 2
                elif ch == "'":
                    if i + 1 < len(s) and s[i + 1] == "'":
                        buf.append("'")
                        i += 2
                    else:
                        i += 1
                        break
                else:
                    buf.append(ch)
                    i += 1
            row.append("".join(buf))
        else:
            m = re.compile(r"NULL|-?[0-9.eE+-]+").match(s, i)
            tok = m.group(0)
            row.append(None if tok == "NULL" else tok)
            i = m.end()
        while s[i] in " \n\r\t":
            i += 1
        if s[i] == ",":
            i += 1
            continue
        if s[i] == ")":
            return row, i + 1
        raise ValueError(f"unexpected char {s[i]!r} at {i}")


def iter_inserts(text):
    """Yield (table, columns, row) for every INSERT INTO statement."""
    head = re.compile(r"INSERT INTO `([^`]+)` \(([^)]*)\) VALUES ")
    pos = 0
    while True:
        m = head.search(text, pos)
        if not m:
            return
        table = m.group(1)
        cols = [c.strip().strip("`") for c in m.group(2).split(",")]
        i = m.end()
        while True:
            row, i = parse_values(text, i)
            yield table, cols, row
            while text[i] in " \n\r\t":
                i += 1
            if text[i] == ",":
                i += 1
                while text[i] in " \n\r\t":
                    i += 1
                continue
            break
        pos = i


def main():
    src, out = sys.argv[1], sys.argv[2]
    text = open(src, encoding="utf-8", errors="replace").read()
    tables = {}
    for table, cols, row in iter_inserts(text):
        if not table.startswith("wp_"):
            continue
        tables.setdefault(table, []).append(dict(zip(cols, row)))
    result = {k: tables.get(k, []) for k in ["wp_posts", "wp_terms", "wp_term_taxonomy", "wp_term_relationships", "wp_options", "wp_postmeta"]}
    json.dump(result, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for k, v in result.items():
        print(f"{k}: {len(v)} rows")


if __name__ == "__main__":
    main()
