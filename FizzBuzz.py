x = int(input("数える数を整数で入力"))
i = 1

for i in range(x):
    i += 1
    if i % 15 == 0:
        print("Fizz Buzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("FIzz")
    else:
        print(i)
