import pyperclip

line = pyperclip.paste()
lines = line.split("\n")

with open("inout/input.txt", "w") as f:
    f.writelines(lines)
