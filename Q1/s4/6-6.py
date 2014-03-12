def factorial(n):
    k = 1
    r = 1
    while k <= n:
        r *= k
        k+=1
    return r

def combinatoria(n, m):
    return factorial(n) / (factorial(m) * factorial(n - m))

print combinatoria(85, 42)
