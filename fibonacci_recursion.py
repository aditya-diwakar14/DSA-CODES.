def fibonacci_rec(n):
    if n <= 1:
        return n
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)

terms = 10
for i in range(terms):
    print(fibonacci_rec(i), end=" ")
