"""
Practical 1 controlled failure.
    python scripts/failure_demo.py break      # commit wrong logic -> CI fails
    python scripts/failure_demo.py restore    # commit fix        -> CI passes
Add --no-push to commit locally only.
"""
import subprocess
import sys
from pathlib import Path

GOOD = 'if internal_marks >= 40 and attendance >= 75:\n        return "PASS"'
BAD = 'if internal_marks >= 40 and attendance >= 75:\n        return "FAIL"'
MSG = {"break": "Modify result logic", "restore": "Fix result prediction bug"}


def run(*cmd):
    print("$", " ".join(cmd))
    subprocess.run(cmd, check=True)


args = [a for a in sys.argv[1:] if not a.startswith("--")]
if len(args) != 1 or args[0] not in MSG:
    sys.exit(__doc__)

path = Path("result_logic.py")
text = path.read_text(encoding="utf-8")
old, new = (GOOD, BAD) if args[0] == "break" else (BAD, GOOD)
if text.count(old) != 1:
    sys.exit("Nothing to change (already in that state?).")
path.write_text(text.replace(old, new), encoding="utf-8")
run("git", "add", "result_logic.py")
run("git", "commit", "-m", MSG[args[0]])
if "--no-push" not in sys.argv:
    run("git", "push", "origin", "main")
