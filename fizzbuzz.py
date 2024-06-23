'''
**Exercise: FizzBuzz**

FizzBuzz is a common coding problem that asks you to print the numbers from 1 to 100. However, there are a couple of exceptions:

1. For multiples of three, print "Fizz" instead of the number.
2. For multiples of five, print "Buzz" instead of the number.
3. For numbers which are multiples of both three and five, print "FizzBuzz".

Try to write a Python program that accomplishes this task using a function with a "for" loop. After you've completed that, try to write the same program but using a "while" loop instead.

Remember to test your code to ensure it's working as expected!

**Hints:**

* You can use the modulus operator `%` to check if a number is a multiple of another number. For example, `n % 3 == 0` checks if `n` is a multiple of 3.
* For the "for" loop, consider using the `range` function.
* For the "while" loop, you'll need to manually increment your counter.


'''

abdullah_test = 1
while abdullah_test <=100:
    if abdullah_test %3 == 0 and abdullah_test %5 ==0:
        print("FizzBuzz")
    elif abdullah_test % 3==0:
        print("Fizz")
    elif abdullah_test % 5 == 0:
        print("Buzz")
    else:
        print(abdullah_test)
    abdullah_test+=1




#!the fizzbuzz core idea or logic 
# if num  % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# elif num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz") 
# else:
#     print(num)  



# for abdullah_test in range(1,101):#start from 1 to 100 the 
#     if abdullah_test % 3 == 0 and abdullah_test % 5 == 0:
#         print("FizzBuzz")
#     elif abdullah_test  % 3 == 0:
#         print("Fizz")
#     elif abdullah_test % 5 == 0:
#         print("Buzz")
#     else:
#         print(abdullah_test)



#print(*map(lambda i: 'Fizz'*(not i%3)+'Buzz'*(not i%5) or i, range(1,101)),sep='\n')


#but it kinda impressive to solve the problem in one line of code
#anthor way to solve the problem using map and lambda function
#but it's not me sloution it's from the internet so i am not going to use it.