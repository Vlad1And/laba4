
a = "змінна з текстом"
b = 1  
b1 = 1.1
c = ["a", 1, 1.25, "Слово", a]  
d = {"a": "Слово", "b": 1, a: b}  
e = ("a", a)  
f = {"ss", str(b) + a}  

print("Строкова змінна:", a)
print("Числова змінна:", b)
print("Список:", c)
print("Словник:", d)
print("Кортеж:", e)
print("Набір:", f)

print("Перша константа:", True)
print(f"І можна так робити вивід? {True}")


print(abs(-12.5), f"є рівним {abs(12.5)}")
print("Максимальне значення у списку:", max(1, 3, 5, 7))
print("Округлене число:", round(3.14159, 2))

letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(f"На позиції {i} знаходиться буква {letters[i]}")


n = 5
while n > 0:
    print(f"Залишилось: {n}")
    n -= 1

A = True
print("Значить А=True" if A else "Значить А=False")

B = 10
if B > 5:
    print("B більше 5")
else:
    print("B менше або рівне 5")

A = 0
try:
    print("Що буде якщо", 10/A, "?")
except Exception as e:
    print(e)
finally:
    print("А вот воно що!")

with open("README.md", "r") as f:
    for line in f:
        print(line)

this_is_lambda = lambda first, last: f'Цей код написав: {first} {last}'
print("Це просто функція:", this_is_lambda)
print("Це її виклик:", this_is_lambda('Владислав', 'Андрес'))

# Приклад простого використання функцій, змінних та циклів
def greet(name):
    return f"Привіт, {name}!"

people = ["Анна", "Іван", "Олена"]
for person in people:
    print(greet(person))

# Виконання математичних операцій
x = 10
y = 3
print(f"{x} поділити на {y} дорівнює {x / y}")
print(f"Ціла частина від ділення {x} на {y} дорівнює {x // y}")