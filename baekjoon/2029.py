A = input().split( )

for i in range(0,len(A)):
    A[i] = int(A[i])

if A == sorted(A):
    print("ascending")
elif A == list(reversed(sorted(A))):
    print("descending")
else :
    print("mixed")
