END = '\u001b[0m'
SET_COLOR = "\x1b[48;5;"

#доп 
import time
import os

def draw_line(offset= 0, lenght=1, color =27):
    line = '  '*lenght
    print(f"{' '*offset}{SET_COLOR}{color}m{line}{END}")

def draw_figure():
    size = 10
    offset = 0
    color =27
    
    while True:
        for placement in range(2):
            if color <200:
                color +=1
            else:
                color-=1
            for line in range(size):
                draw_line(offset, size,color)
                
            if offset==0:
                offset+=1
            else:
                offset-=1
            time.sleep(0.4)
            os.system('cls')

draw_figure()