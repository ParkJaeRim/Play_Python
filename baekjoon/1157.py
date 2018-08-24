from collections import Counter

n = input().upper()
if len(n)==1:
    print(n)
else:
    mode = Counter(n).most_common(2)
    
    if mode[0][1] ==  mode[1][1]:
        print("?")
    else: 
        print(mode[0][0])
