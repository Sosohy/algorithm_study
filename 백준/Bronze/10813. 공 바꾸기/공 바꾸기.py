n , m = map(int, input().split())

basket = [i for i in range(1, n+1)]

for i in range(m):
    s, e = map(int, input().split())
    s -= 1
    e -= 1
    basket[s], basket[e] = basket[e], basket[s]

print(" ".join(map(str, basket)))
