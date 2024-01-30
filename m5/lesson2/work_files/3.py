# напиши код для выполнения заданий здесь
# задание 3
count = 0
with open('my_file.txt', 'r') as file:
    for string in file:
        string_list = string.split(' ')
        for symbol in string_list:
            count += int(symbol)
print('Сумма всех чисел: ', count)
