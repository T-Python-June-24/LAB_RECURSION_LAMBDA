# # Bonus (solve in a new file)

# **Exercise: FizzBuzz**

# FizzBuzz is a common coding problem that asks you to print the numbers from 1 to 100. 
# However, there are a couple of exceptions:

# 1. For multiples of three, print "Fizz" instead of the number.
# 2. For multiples of five, print "Buzz" instead of the number.
# 3. For numbers which are multiples of both three and five, print "FizzBuzz".

# Try to write a Python program that accomplishes this task using a function with a "for" loop. 
# After you've completed that, try to write the same program but using a "while" loop instead.

# Remember to test your code to ensure it's working as expected!

# **Hints:**

# * You can use the modulus operator `%` to check if a number is a multiple of another number. 
#           For example, `n % 3 == 0` checks if `n` is a multiple of 3.
# * For the "for" loop, consider using the `range` function.
# * For the "while" loop, you'll need to manually increment your counter.




def FizzBuzz1():
    for i in range(1, 101):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%5 == 0:
            print("Buzz")
        elif i%3 == 0:
            print("Fizz")
        else:
            print(i)

FizzBuzz1()

print("\n\n\n*****\n\n\n")

def FizzBuzz2():
    i = 1
    while i <= 100:
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%5 == 0:
            print("Buzz")
        elif i%3 == 0:
            print("Fizz")
        else:
            print(i)
        i +=1


FizzBuzz2()