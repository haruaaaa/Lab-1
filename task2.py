END = '\u001b[0m'
SET_COLOR = "\x1b[48;5;"

#2
#общие параметры
step = 10 #длина пробелов
count = 9 
color = 28

def draw_pattern1():
    print(f"{' '*step}{SET_COLOR}{color}m  {END}" *count)

def fill():
    print(f'{SET_COLOR}{color}m{' '*step*(count+2)}{END}')

def draw_pattern2():
    print(f"{' '*int(step/2)}{SET_COLOR}{color}m  {END}" + f"{' '*step}{SET_COLOR}{color}m  {END}"*(count-1))

#рисование узора
for i in range(3):
    fill()
    draw_pattern1()
    fill()
    draw_pattern2()
fill()

