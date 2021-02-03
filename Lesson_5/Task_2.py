# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


my_file = open('test_2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('test_2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('test_2.txt', 'r')
content = my_file.read().splitlines()
wordcount = []
for line in range(len(content)):
    content[line] = content[line].split()
    wordcount.append(len(content[line]))
print("Количество слов в строках:", *wordcount, sep = "\n")
my_file.close()