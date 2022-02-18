num = int(input())
score = 0
for i in range(1,num+1):
    if (i<100):
        score += 1
    else:
        seat = list(map(int, str(i)))
        if seat[0] - seat[1] == seat[1] - seat[2]:
        # if (i%10 - (i%100)/10) == ((i%100)/10 - i/100):
            score +=1
print(score)
