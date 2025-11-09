import pyperclip

saikikeisatu = [
    " ■■■■■■■■■■■    ■ ■■■■■■  ■■■■■■■ ■          ■          ■      ■       ■ ",
    "      ■         ■      ■    ■     ■■■■  ■■■■■■■■■■■     ■     ■■       ■ ",
    "  ■■■■■■■■■  ■■ ■ ■■■■■■   ■■■■■■■■ ■   ■         ■  ■■■■■■■■          ■ ",
    "  ■   ■   ■  ■■ ■ ■■■■■■   ■■■■ ■  ■■     ■■■■■■■■■    ■■              ■ ",
    "  ■   ■   ■  ■■ ■           ■■■■■■■■■■   ■■ ■ ■  ■     ■               ■ ",
    "  ■■■■■■■■■  ■■ ■■■■■■■■■    ■■■■■■■    ■■ ■   ■■      ■  ■■■■■        ■ ",
    "  ■   ■   ■  ■■ ■■   ■   ■■■■■■■■■■■■■■  ■■■■■■■■■     ■  ■■■          ■ ",
    "■■■■■■■■■■■■■  ■■■■■■■■■■   ■■■■■■■■■   ■■■■■■■■■■■   ■■               ■ ",
    "  ■       ■    ■  ■  ■  ■   ■■■■■■■■■        ■  ■     ■                  ",
    "  ■       ■    ■  ■  ■  ■   ■■■■■■■■■    ■■  ■   ■    ■   ■              ",
    "  ■       ■   ■■  ■  ■ ■■   ■       ■   ■■   ■    ■  ■■   ■            ■ ",
    "  ■     ■■■   ■      ■      ■■■■■■■■■      ■■■       ■    ■■■■■■       ■ ",
]


from typing import List
with open("answer.py", "r", encoding="utf-8") as f:
    lines: List[str] = f.readlines()
    dfsflag = False
    pypyflag = False
    for line in lines:
        if "dfs" in line: dfsflag = True
        if "pypy" in line: pypyflag = True

    if dfsflag and not pypyflag:
        for s in saikikeisatu:
            print(s)
        print("\"dfs\"を検知しました。おまじないが必要かも。")
        exit()
    text = "".join(lines)
    pyperclip.copy(text)