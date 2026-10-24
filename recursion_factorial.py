"""this is a recursion method of python, where recursion means a function calls itself again and again
where 2 points are main:-
1. we have to put a base value, here in our function we have put base values of n==0 and n==1 is 1, 
puting a base value is a full stop of a recursive function otherwise it will call itself infinite times, and throw an error.
2. the formula we will use for recursion should reduce as it calls itself, so that it cal lead towards the base value.
"""

def factorial(n):
    if(n==0 or n==1): # base value initialisation
        return 1
    else:
        return n*factorial(n-1) # a formula which reduces itself over and over again as the function is called
n= int(input("give number to find factorial :"))
print(f"factorial of {n} is :",factorial(n)) # use of f-strings