# Создайте список квадратов этих чисел, используя list comprehension
squares = [x ** 2 for x in range(1, 11)]
# print(squares)
# Список чётных
even_numbers = [x for x in range(1, 20) if x % 2 == 0]
print(even_numbers)