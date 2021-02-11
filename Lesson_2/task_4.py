#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

user_words = input("Введите несколько слов через пробел ")
words_count = user_words.split(" ")
lengths = [len(i) for i in words_count]
biggest = max(lengths)
if biggest < 10:
    for i, item in enumerate(words_count):
        print(i + 1, item)
else:
    print("Длинный элемент, вывод первых 10 символов")
    for i, item in enumerate(words_count [0:10]):
        print(i + 1, item [0:10])