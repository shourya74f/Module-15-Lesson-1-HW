n=5
f=n*(n+1)//2
print("Total points:", f)

l=0
s=0
for i in range(1, n+1):
    l+=i
    s+=1
print("Total loop points: ", l)
print("Total step points: ", s)

ne=0
sn=0
for i in range(1, n+1):
    for j in range(1, i+1):
        ne+=1
        sn+=1
print("Total nested loop points: ", n)
print("Total nested step points: ", sn)