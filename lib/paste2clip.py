import pyperclip

with open("answer.py", "r", encoding="utf-8") as f:
    lines = f.readlines()
    text = "".join(lines)
    pyperclip.copy(text)