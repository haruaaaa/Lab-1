#3
#создаю пустую координатную плоскость(её поле значений)
field = [[0 for i in range(11)] for i in range(11)]

x = [] 
#ось x
for i in range(0,101,10):
    x.append(i)

y = [i for i in range(11)]
#ось y

#переход из х в результат
results = [0 for i in range(11)]
for i in range(11):
    results[i] = round(x[i]**0.5)

#заполняем поле соответствием значений с результатом
for i in range(11):
    for j in range(11):
        if results[i]==y[j]:
            field[j][i] = 1

#строим график функции
for i in range(11):
    line = ''
    for j in range(12):
        if j==0:
            line += '\t' + str(y[10-i]) + '\t'
        else:
            if field[10-i][j-1] == 0: 
                line += '---'
            if field[10-i][j-1] == 1:
                line += '@@@'
    print(line)
print('\t\t  0 10 20 30 40 50 60 70 80 90 100')
