def multiplesForLoop(n=100):
    for i in range(0,n+1):
        if i%3==0:
            print("Fizz")
        elif i%5:
            print("Buzz")
        elif i%5==0 and i%3==0:
            print("FizzBuzz")
def multiplesWhileLoop(n=100):
    i=0
    while True:
        if i%3==0:
            print("Fizz")
        elif i%5:
            print("Buzz")
        elif i%5==0 and i%3==0:
            print("FizzBuzz")
        if i==100:
            break
        i+=1
multiplesWhileLoop()

