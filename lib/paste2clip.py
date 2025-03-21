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
    for line in lines:
        if "dfs" in line:
            for s in saikikeisatu:
                print(s)
            choice = input("\"dfs\"を検知しました。おまじないを書きましたか？ [y/N] :").lower()
            if choice in ['y', 'ye', 'yes']:
                break
            elif choice in ['n', 'no']:
                exit()
    text = "".join(lines)
    pyperclip.copy(text)