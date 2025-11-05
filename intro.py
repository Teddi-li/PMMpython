# console_notepad.py
from pathlib import Path

fname = input("File name (Enter=notes.txt): ").strip() 
print("Type your notes. Type ::end on its own line to finish.\n")

lines = []
while True:
    line = input()
    if line.strip() == "::":
        break
    lines.append(line + "\n")

Path(fname).write_text("".join(lines), encoding="utf-8")
print(f"Saved to {Path(fname).resolve()}")
