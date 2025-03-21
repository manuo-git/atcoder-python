import pyperclip

line = pyperclip.paste()
lines = line.split("\n")

with open("inout/input.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
