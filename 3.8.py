num = int(input("Enter the number for the times table: "))
if num < 0:
    num = abs(num)
    for i in range(12, -1, -1):
        print(str(num) + " x " + str(i) + " = " + str(num * i))
else:
        for i in range(0, 13):
            print(str(num) + " x " + str(i) + " = " + str(num))