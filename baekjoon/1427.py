n =input()
hi = []

for i in range(len(n)):
    hi.append(n[i])
    hi[i] = int(hi[i])
    hi = list(reversed(sorted(hi)))

for j in range(len(hi)):
    print(hi[j], end='')
