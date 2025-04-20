
a = int(input("Довжина лінії: "))
b = input("Cимвол: ")

for _ in range(a):
    print(b)


while True:
    number = float(input("Введіть число: "))
    
    if number > 0:
        print("Number is positive")
    elif number < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")

    if number == 7:
        print("Good bye!")
        break


numbers = []
while True:
    number = int(input("Введіть число: "))
    numbers.append(number)

    if number == 7:
        print("Good bye!")
        break

if numbers:
    print(f"Сума: {sum(numbers)}")
    print(f"Макc: {max(numbers)}")
    print(f"Мін: {min(numbers)}")
