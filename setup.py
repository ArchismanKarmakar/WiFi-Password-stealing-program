from cx_Freeze import setup, Executable

file = open("main.py", "a", encoding="utf-8")
r1 = random.randint(-100000, 100000)
file.write("\nvar = " + r1)
file.write("\nprint(var)\n")
file.close()