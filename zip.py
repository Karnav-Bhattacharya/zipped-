s, n = list(map(int, input().split()))
ns = []
for i in range(n):
    ns.append(list(map(float, input().split())))

ns = zip(*ns)
print('\n'.join(str(sum(x)/len(x)) for x in ns))
