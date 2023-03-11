file = open('text_file.txt', 'r', encoding='UTF-8')
text = file.readlines()
print(text)
file.close()