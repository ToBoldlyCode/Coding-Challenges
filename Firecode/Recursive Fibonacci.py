def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return n + fib(n - 1)