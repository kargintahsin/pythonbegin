a = 10  # global


def function():
    a = 5  # local
    print(a)


function()
print(a)
# variable a 's global value 10 and local value 5. So if use in function, a=5 but out of function, a=10
print("PART 2")

b = 10


def function2():
    global b
    b = 5
    print(b)


print(b)
function2()
# if you use "global" word for a variable in a function, that's mean you use variable's global version.
