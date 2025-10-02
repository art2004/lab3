from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction
from datetime import datetime
# 1. Создайте список квадратов этих чисел, используя list comprehension
squares = [x ** 2 for x in range(1, 11)]
# print(squares)
# 2. Список чётных
even_numbers = [x for x in range(1, 20) if x % 2 == 0]
# print(even_numbers)
# 3. Создайте новый список, где все слова будут в верхнем регистре и длинее 3 символов.
words = ["python", "Java", "c++", "Rust", "go"]
upper_long3_words = [word.upper() for word in words if len(word) > 3]
# print(upper_long3_words)
# 4. Создайте класс-итератор Countdown, который принимает число и при итерации возвращает числа от этого числа до 1
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

#for x in Countdown(30):
    #print(x)

# 5. Напишите итератор fibonacci(n), который возвращает первые n чисел Фибоначчи.
class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result

#for num in Fibonacci(7):
    #print(num)
# 6.  Посчитать вклад

# P = Decimal(input('Введите начальную сумму вклада: '))
# r = Decimal(input('Введите процентную ставку. Пример 7.5: '))
# t = Decimal(input('Введите срок в годах: '))
#
# # Формула: S = P * (1 + r/(12*100))^(t*12)
# monthly_rate = (r / Decimal('1200'))  # Делим на 1200, чтобы получить месячную ставку
# S = P * (Decimal('1') + monthly_rate) ** (t * Decimal('12'))
# S = S.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)  # Округление до копеек
#
# profit = S - P
# profit = profit.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
#
# print(f"Итоговая сумма: {S} руб.")
# print(f"Прибыль: {profit} руб.")

# 7. Дроби
# a = Fraction(3, 4)
# b = Fraction(5, 6)
#
# print(f"Сложение: {a + b}")
# print(f"Вычитание: {a - b}")
# print(f"Умножение: {a * b}")
# print(f"Деление: {a / b}")

# 8. Текущая дата
# now = datetime.now()
# print(f"Текущая дата и время: {now}")
# print(f"Только текущая дата: {now.date()}")
# print(f"Только текущее время: {now.time()}")

# 9. # Разница в днях

birth_date = datetime(2004, 12, 24)
today = datetime.now() # Текущая дата и время


days_passed = (today - birth_date).days
print(f"Дней прошло с момента рождения: {days_passed}")

next_birthday = datetime(today.year, 12, 24)
if today > next_birthday:
    next_birthday = datetime(today.year + 1, 12, 24)
days_to_birthday = (next_birthday - today).days
print(f"Дней до следующего дня рождения: {days_to_birthday}")