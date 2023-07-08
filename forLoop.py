# Factorial calculator with forLoop

factorial = 1

while True:
    sayi = int(input("Enter a positive number: "))
    if sayi <= 0:
        print("You entered a non-positive number.")
    else:
        for i in range(1, sayi + 1):
            factorial = factorial * i

        print("Factorial: ", factorial)
        break
