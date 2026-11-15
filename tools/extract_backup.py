"""Stream a WordPress MySQL backup and extract content tables to JSON (no SQL is executed).

Usage: python extract_backup.py <backup.sql> <outdir>
Column names come from the CREATE TABLE statements in the dump, because this dump's
INSERTs have no column list. wp_users and wp_usermeta are deliberately skipped.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from parse_wp_dump import parse_values  # noqa: E402

WANTED = {"wp_posts", "wp_comments", "wp_terms", "wp_term_taxonomy", "wp_term_relationships",
          "wp_options", "wp_postmeta", "wp_redirection_items", "wp_redirection_404", "wp_users"}
CREATE_RE = re.compile(r"^CREATE TABLE `([^`]+)`")
COL_RE = re.compile(r"^\s+`([^`]+)`\s")
INSERT_RE = re.compile(r"^INSERT INTO `([^`]+)` VALUES ")


def main():
    src, outdir = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    cols, rows = {}, {t: [] for t in WANTED}
    current = None
    seen = 0
    with open(src, encoding="utf-8", errors="replace") as f:
        for line in f:
            seen += 1
            if current:
                if line.startswith(") ENGINE"):
                    current = None
                else:
                    m = COL_RE.match(line)
                    if m:
                        cols[current].append(m.group(1))
                continue
            m = CREATE_RE.match(line)
            if m and m.group(1) in WANTED:
                current = m.group(1)
                cols[current] = []
                continue
            m = INSERT_RE.match(line)
            if not m or m.group(1) not in WANTED:
                continue
            table = m.group(1)
            i = m.end()
            while True:
                row, i = parse_values(line, i)
                rows[table].append(dict(zip(cols[table], row)))
                while line[i] in " \n\r\t":
                    i += 1
                if line[i] == ",":
                    i += 1
                    while line[i] in " \n\r\t":
                        i += 1
                    continue
                break
            if seen % 100000 == 0:
                print("lines", seen, flush=True)
    # Only public author-archive fields: no email, password hash, login or registration data.
    rows["wp_users"] = [{k: r.get(k) for k in ("ID", "user_nicename", "display_name")} for r in rows["wp_users"]]
    for t in sorted(WANTED):
        with open(os.path.join(outdir, f"{t}.json"), "w", encoding="utf-8") as out:
            json.dump(rows[t], out, ensure_ascii=False)
        print(t, "columns", len(cols.get(t, [])), "rows", len(rows[t]), flush=True)


if __name__ == "__main__":
    main()
