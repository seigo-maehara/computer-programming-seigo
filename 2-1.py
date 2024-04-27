def Fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-2) + Fibonacci(n-1)

exec(input())
