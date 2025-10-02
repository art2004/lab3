# Создайте список квадратов этих чисел, используя list comprehension
squares = [x ** 2 for x in range(1, 11)]
# print(squares)
# Список чётных
even_numbers = [x for x in range(1, 20) if x % 2 == 0]
# print(even_numbers)
# Создайте новый список, где все слова будут в верхнем регистре и длинее 3 символов.
words = ["python", "Java", "c++", "Rust", "go"]
upper_long3_words = [word.upper() for word in words if len(word) > 3]
print(upper_long3_words)