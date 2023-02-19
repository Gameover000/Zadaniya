def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a


o = int(input())
for f in range(2, o+1):
    if is_prime(f):
        print(f)