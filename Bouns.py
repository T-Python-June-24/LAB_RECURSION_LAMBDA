for num in range(1,100):
    stringValue = " "
    if num % 3 == 0:
        stringValue += "Fizz"
    if num % 5 == 0: 
        stringValue += "Buzz"
    if num % 3 != 0 and num % 5 != 0 :
        stringValue += str(num)

    print(stringValue)

num = 1
while  num <= 100:
    stringValue = " "
    if num % 3 == 0:
        stringValue += "Fizz"
    if num % 5 == 0: 
        stringValue += "Buzz"
    if num % 3 != 0 and num % 5 != 0:
        stringValue += str(num)
    print(stringValue)
    num += 1

