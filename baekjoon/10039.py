score =[]
sums = 0
means = 0

for i in range(0,5):
    score.append(input())
    score[i] = int(score[i])
    if score[i] < 40:
        score[i] = 40
    sums += score[i]
    means = sums/5
print(int(means))
