def fact(n):
    if n > 0:
        return n * fact(n-1)
    return 1  # Corrected base case

res = fact(5)
print(res)