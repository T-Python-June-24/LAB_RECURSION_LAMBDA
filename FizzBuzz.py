# FizzBuzz using a for loop

for x in range(1,100):
    if x%3 == 0 and not x%5 == 0:
        print("Fizz")
    elif x%5 == 0 and not x%3 == 0:
        print("Buzz")
    elif x%3 == 0 and x%5 == 0:
        print("FizzBuzz")
    else:
        print(x)

# FizzBuzz using a while loop

x = 0
while x != 100:
    x += 1
    if x%3 == 0 and not x%5 == 0:
        print("Fizz")
    elif x%5 == 0 and not x%3 == 0:
        print("Buzz")
    elif x%3 == 0 and x%5 == 0:
        print("FizzBuzz")
    else:
        print(x)