import time 

SET_COLOR = "\x1b[48;5;"
END = '\x1b[0m'
CLEAR = "\033[H"

def draw_line(offset= 0, lenght=1, color =222):
    line = ' '*lenght
    print(f"{' '*offset}{SET_COLOR}{color}m{line}{END}")
    
def draw_romb():
    size = 15
    center = size//2
    offset = size//2

    step =1
    lenght = 1

    colors = [52, 107]

    while True:
        for color in colors:
            for line in range(size):
                draw_line(offset, lenght, color)

                if line < center:
                    offset -= step
                    lenght += step*2
                else:
                    lenght -= step*2
                    offset += step

            print(f'\x1b[{size+2}A')
            print(f'\x1b[{offset}D')

            lenght = 1
            offset = size//2

            time.sleep(1)

draw_romb()
# if __name__ == "__main__":
#     for i in range(40):
#         draw_line(lenght=44, color=109,offset=i)
#         print(f'{CLEAR}')
#         time.sleep(0.5)