lines = []

with open("C:\\Users\\manuo\\AppData\\Roaming\\Code\\User\\snippets\\python.json", encoding="utf-8") as f:
    lines = f.readlines()

with open("M:\\PythonScripts\\atcoder\\python\\snippets.json", "w", encoding="utf-8") as f:
    f.writelines(lines)
