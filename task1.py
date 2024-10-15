RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
SET_COLOR = "\x1b[48;5;"

#1
for i in range(2):
    print(f"{WHITE}{' '*30}{END}")
for i in range(2):
    print(f"{RED}{' '*30}{END}")

