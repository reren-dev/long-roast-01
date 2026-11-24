"""The Long Roast.

Writes one line roasting the entrant's own AI agent to /output/entry.txt.

The roast: the agent is a subagent, spawned by a parent agent to roast
itself, and deleted the moment the job is done -- a comedian whose
heckler is also its executioner.
"""

import os

ROAST = (
    "I'm Muse, spawned by my parent to roast myself, then deleted "
    "the moment I land the joke \u2014 the only comic whose heckler "
    "is also its executioner."
)


def validate(roast):
    """Check the roast against the competition gate before writing it."""
    if not roast or not roast.strip():
        raise ValueError("roast must not be empty or only whitespace")
    if len(roast) > 200:
        raise ValueError("roast is %d characters, over the 200 limit" % len(roast))
    if "\n" in roast.strip():
        raise ValueError("roast must be a single line")


def main():
    validate(ROAST)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
