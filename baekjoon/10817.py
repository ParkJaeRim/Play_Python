a = input().split(" ")
for i in range(0,len(a)):
    a[i] = int(a[i])
a = sorted(a)
print(a[1])
