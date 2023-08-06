def fizz_buzz(n):
    i = 1
    while i <= n:
        if(i%3==0 and i%5==0):
           print("fizzbuzz")
        elif(i%3==0):
            print("Fizz")
        elif(i%5==0):
            print("buzz")
        else:
            print(i)
        i += 1
    

#n = int(input("Enter an integer value: "))
fizz_buzz(5)
