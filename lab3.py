# Создайте список квадратов этих чисел, используя list comprehension
squares = [x ** 2 for x in range(1, 11)]
# print(squares)
# Список чётных
even_numbers = [x for x in range(1, 20) if x % 2 == 0]
# print(even_numbers)
# Создайте новый список, где все слова будут в верхнем регистре и длинее 3 символов.
words = ["python", "Java", "c++", "Rust", "go"]
upper_long3_words = [word.upper() for word in words if len(word) > 3]
# print(upper_long3_words)
# Создайте класс-итератор Countdown, который принимает число и при итерации возвращает числа от этого числа до 1
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        result = self.current
        self.current -= 1
        return result

for x in Countdown(30):
    print(x)