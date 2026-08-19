import json
import re
from pathlib import Path


def first_h1(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if re.match(r"^#\s+", line):
                return re.sub(r"^#\s+", "", line)

    return path.stem


ROOT = Path(".")
modules_data = []

for module_dir in sorted(ROOT.glob("module*")):

    if not module_dir.is_dir():
        continue

    overview_file = next(
        module_dir.glob("00_*.md"),
        None
    )

    if not overview_file:
        continue

    module_title = first_h1(overview_file)

    lecture_files = sorted(
        [
            f for f in module_dir.glob("*.md")
            if not f.name.startswith("00_")
        ]
    )

    lectures = []

    for lecture in lecture_files:

        lectures.append({
            "file": lecture.name,
            "title": first_h1(lecture)
        })

    modules_data.append({
        "folder": module_dir.name,
        "title": module_title,
        "lectures": lectures
    })

manifest = {
    "modules": modules_data
}

with open(
    "manifest.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        manifest,
        f,
        indent=4,
        ensure_ascii=False
    )

print("manifest.json generated")