# For loop solution
print("For loop:")
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0 :
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)

# While loop solution
print("While loop:")
x = 1
while x < 101:
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0 :
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
    x += 1