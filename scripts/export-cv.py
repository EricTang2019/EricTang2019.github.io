#!/usr/bin/env python3
"""Compile a public CV from a private Overleaf checkout, without changing it."""

import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Path to the canonical Overleaf checkout")
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "files/Jingwu_Tang_CV.pdf")
    args = parser.parse_args()
    source = args.source.resolve()
    latexmk = shutil.which("latexmk")
    if not latexmk and Path("/Library/TeX/texbin/latexmk").exists():
        latexmk = "/Library/TeX/texbin/latexmk"
    if not latexmk:
        parser.error("latexmk is required (install a TeX distribution).")
    if not (source / "main.tex").is_file():
        parser.error("The Overleaf checkout must contain main.tex.")

    with tempfile.TemporaryDirectory(prefix="jingwu-public-cv-") as temp:
        working = Path(temp) / "source"
        shutil.copytree(source, working, ignore=shutil.ignore_patterns(".git", "*.pdf", "*.log", "*.aux", "*.out", "*.fls", "*.fdb_latexmk"))
        main_tex = working / "main.tex"
        text = main_tex.read_text()
        # Export only the professional email and website from the contact section.
        # The private source retains its full contact details.
        contact_pattern = r"(\\section\{\\sc Contact Information\}\s*\n)(.*?)(?=\\section\{)"
        match = re.search(contact_pattern, text, flags=re.S)
        if not match:
            parser.error("Contact section not recognized; review it before exporting.")
        contact_lines = []
        for line in match.group(2).splitlines():
            if line.lstrip().startswith("%"):
                continue
            if "@" in line or (r"\href{https://" in line and "tangjingwu.com" in line):
                contact_lines.append(line)
        if not contact_lines or not any("@" in line for line in contact_lines):
            parser.error("Could not find the professional email in the contact section.")
        text = text[:match.start(2)] + "\n".join(contact_lines) + "\n\n" + text[match.end(2):]
        main_tex.write_text(text)
        env = dict(os.environ)
        env["PATH"] = str(Path(latexmk).parent) + os.pathsep + env.get("PATH", "")
        result = subprocess.run([latexmk, "-pdf", "-interaction=nonstopmode", "-halt-on-error", "-no-shell-escape", "main.tex"], cwd=working, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if result.returncode:
            raise SystemExit("CV compilation failed:\n" + "\n".join(result.stdout.splitlines()[-35:]))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(working / "main.pdf", args.output)
    print(f"Public CV exported to {args.output}")


if __name__ == "__main__":
    main()
