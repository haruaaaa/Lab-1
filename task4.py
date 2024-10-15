END = '\u001b[0m'
SET_COLOR = "\x1b[48;5;"

#4
file_list = [float(i) for i in open('sequence.txt')]

#найдём первое среднее значение
count1 = []
for i in range(125):
    count1.append(abs(file_list[i]))
count1 = sum(count1)/125

#найдём второе среднее значение
count2 = []
for i in range(125,250):
    count2.append(abs(file_list[i]))
count2 = sum(count2)/125

print(f"среднее 1: {SET_COLOR}10m{' '*round(count1*10)}{END}")
print(f"среднее 2: {SET_COLOR}14m{' '*round(count2*10)}{END}")