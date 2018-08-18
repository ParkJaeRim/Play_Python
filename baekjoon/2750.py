n = int(input())
score = []

for i in range(0,n):
    score.append(input())
    score[i] = int(score[i])
    score = sorted(score)

for j in range(0,len(score)):
    print(score[j])
