
def fizzBuzzA():
    for number in range(1,100):
        if number % 3 == 0 and number % 5 == 0:
            print ("FizzBuzz")
        elif number % 3 == 0:
            print ("Fizz")
        elif number % 5 == 0:
            print ("Buzz")
        else:
            print(number)

fizzBuzzA()



def fizzBuzzB():
    number = 1
    while number < 100:
        if number % 3 == 0 and number % 5 == 0:
            print ("FizzBuzz")
        elif number % 3 == 0:
            print ("Fizz")
        elif number % 5 == 0:
            print ("Buzz")
        else:
            print(number)
        number+=1


fizzBuzzB()


def fizzBuzzC(number):
    if number <= 100 and number > 0:
        if number % 3 == 0 and number % 5 == 0:
            print ("FizzBuzz")
        elif number % 3 == 0:
            print ("Fizz")
        elif number % 5 == 0:
            print ("Buzz")
        else:
            print(number)
        fizzBuzzC(number -1)
        


fizzBuzzC(100)