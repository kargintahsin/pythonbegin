# Factorial calculator
def def_factorial(num1):
    factorial = 1
    for i in range(1, num1 + 1):
        factorial *= i
    # print(factorial)
    return factorial


number = int(input("Enter a number: "))
x = def_factorial(number)
print("factorial: ", x)


# Personal Information
def acount(name="None", surname="None", age="None"):
    print("Name: {}\nSurname: {}\nAge: {}".format(name, surname, age))


acount("Tahsin", age=20)
