# напиши код для выполнения заданий здесь
# задание 5

count = 0
max_elem = 0
with open('my_file.txt', 'r') as file:
    lines = file.readlines()
    for s in range(len(lines)):
        string_list = lines[s].split(' ')
        for i in range(len(string_list)):
            if int(string_list[i]) > max_elem:
                max_elem = int(string_list[i])

        count += max_elem
        max_elem = 0

print('Сумма максимальных значений каждой строки: ', count)
