# Q1
# Find the discount #
"""
def dis(price, discountPercentage):
    newPrice = price - (price * (discountPercentage / 100))
    return newPrice


price = int(input("Enter price: "))
discountPercentage = int(input("Enter discount: "))
newPrice = dis(price, discountPercentage)
print("New price is:", newPrice)

-------------------------------------------------------------------------------
# Q2
# Find the Highest integer #


def find_highest(lst):
    highestValue = None
    for i in lst:
        if highestValue is None:
            highestValue = i
        elif i > highestValue:
            highestValue = i
    return highestValue


print(find_highest([-1, 3, 5, 6, 19, 12, 2]))

-------------------------------------------------------------------------------

# Q3
# Sum of Odd and Even Numbers int list #
listx = [1, 2, 3, 4, 5, 6, 7, 8]


def sumOddAndEven(list1):
    sumOdd = 0
    sumEven = 0
    for i in list1:
        if i % 2 == 0:
            sumEven += i
        else:
            sumOdd += i
    lastList: list[int] = [sumEven, sumOdd]
    return lastList


print(sumOddAndEven(listx))

-------------------------------------------------------------------------------

# Q4
# Interview Controller #
timeList1 = [5, 5, 10, 10, 15, 15, 20, 20]
totalTime1 = 120


def interview(timeList, totalTime):
    qTime = 0
    qualified = "Qualified"
    disqualified = "Disqualified"
    if len(timeList) != 8 or totalTime > 120:
        return disqualified
    else:
        for i in timeList[:2]:
            qTime = i
            if i > qTime:
                qTime = i
            elif qTime > 5:
                return disqualified
        for i in timeList[2:4]:
            qTime = i
            if i > qTime:
                qTime = i
            elif qTime > 10:
                return disqualified
        for i in timeList[4:6]:
            qTime = i
            if i > qTime:
                qTime = i
            elif qTime > 15:
                return disqualified
        for i in timeList[6:]:
            qTime = i
            if i > qTime:
                qTime = i
            elif qTime > 20:
                return disqualified
        return qualified


result = interview(timeList1, totalTime1)
print(result)

-------------------------------------------------------------------------------
"""
