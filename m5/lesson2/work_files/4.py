# напиши код для выполнения заданий здесь
# задание 4
count = 0
with open('my_file.txt', 'r') as file:
    lines = file.readlines()
    for s in range(len(lines)):
        string_list = lines[s].split(' ')
        for elem in range(len(string_list)):
            if s == 2 or s == 5 or s == 8 or s == 11:
                count += int(string_list[elem])
print('Сумма 3, 6, 9, 12 строк: ', count)
