a = int(input("Перша цифра: "))
b = int(input("Друга цифра: "))
c = int(input("Третя цифра: "))

num = a * 100 + b * 10 + c

print("Число:", num)



num = int(input("Введіть чотирьохзначне число: "))


a = num // 1000
b = (num // 100) % 10
c = (num // 10) % 10
d = num % 10

dob = a * b * c * d

print("Добуток:", dob)



metri = int(input("Кількість метрів: "))

cen = metri * 100
dec = metri * 10
mil = metri * 1000
mile = metri / 1609.34

print("У сантиметрах:", cen)
print("У дециметрах:", dec)
print("У міліметрах:", mil)
print("У милях:", mile)
print(f"У сантиметрах: {cen}, У дециметрах: {dec}, У міліметрах: {mil}, У милях: {mile}")



a = int(input("розмір основи трикутника: "))
b = int(input("розмір висоти трикутника: "))

plo = 0.5 * a * b

print("Площа трикутника:", plo)



