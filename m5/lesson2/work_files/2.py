# напиши код для выполнения заданий здесь
# задание 2
with open('my_file.txt', 'r') as file:
    lines = file.readlines()
    second_line = lines[13].split(' ')
    result = int(second_line[7])
    print(result)

