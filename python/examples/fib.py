def fib(n):
    """Calculates the Fibonacci sequence up to n."""
    res = []
    a, b = 0, 1

    while a < n:
        res.append(a)
        a, b = b, a + b

    return res
