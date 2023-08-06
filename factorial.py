def Factorial(n):
    if(n==0):
        return 1
    return n*Factorial(n-1)

print(str(5) + "! = " + str(Factorial(5)))