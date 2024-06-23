def FizzBuzz_f(num:int):
 for i in range(1 , num+1):
    if i %3 ==0:
        print("Fizz")
    elif i % 5 ==0:
        print("Buzz")
    elif i %3 ==0 and i%5==0:
        print("FizzBuzz")
    else:
        print(i)

FizzBuzz_f(100)

def FizzBuzz_w(num:int):
   number=1
   while number <=num:
        if number % 3 ==0:
            print("Fizz")
        elif number % 5 ==0:
            print("Buzz")
        elif number %3 ==0 and number%5==0:
            print("FizzBuzz")
        else:
            print(number)
        number+=1
FizzBuzz_w(100)
