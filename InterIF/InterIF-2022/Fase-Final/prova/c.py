n,x,y = (int(x) for x in input().split(" "))

# aurora = [int (x) for x in input().split(" ")]
# breno = [int (x) for x in input().split(" ")]

figs = [int (x) for x in input().split(" ")]
aurora = [0] * n
breno = [0] * n

for fig in figs:
    aurora[fig-1] += 1

figs = [int (x) for x in input().split(" ")]

for fig in figs:
    breno[fig-1] += 1

auroraPeg = 0
brenoPeg = 0
auroraFt = 0
brenoFt = 0

for i in range(n):
    if(aurora[i] == 0):
        auroraFt+=1
        if(breno[i] > 1):
            auroraPeg+=1
    if(breno[i] == 0):
        brenoFt+=1
        if(aurora[i] > 1):
            brenoPeg+=1

menor = min(auroraPeg, brenoPeg)

print(auroraFt - menor)
print(brenoFt - menor)
    

