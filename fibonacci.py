def fibonacci(cycles):
    if cycles == 0:     #2 base cases
        return 0
    if cycles == 1:
        return 1
    answer = fibonacci(cycles-1) + fibonacci(cycles-2)
    return answer

print("Number of bunnies after 12 months: ", fibonacci(12))