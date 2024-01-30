# напиши код для выполнения заданий здесь
# задание 1
count = 0
with open('my_file.txt', 'r') as file:
    for string in file:
        string_list = string.split(' ')
        for symbol in string_list:
            if int(symbol) == 1:
                count += 1
print('Единиц: ', count)
