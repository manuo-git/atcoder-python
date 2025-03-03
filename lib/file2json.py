f = open("answer.py", mode = "r", encoding="utf-8")
lines = f.readlines()
g = open("lib/result.txt", mode = "w", encoding="utf-8")
for li in lines:
    nli = "\""
    for c in li:
        if c == "\t":
            nli += "    "
        elif c == "\n":
            break
        else:
            nli += c
    nli += "\",\n"
    g.write(nli)