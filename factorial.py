def factorial(n):
    if n == 0:          #n==1 is NOT a base case
        return 1
    answer = n*factorial(n-1) 
    return answer
    #fact(n) = n * fact(n-1)
    #fact(n-1) = n-1 * fact(n-2)

print("Enter number for factorial: ")
print(factorial(int(input())))
