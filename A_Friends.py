a=int(input())
b=int(input())

if a>b:
    a,b=b,a
t=0
count=1
while a!=b:

    if b-a!=1:
        a+=1
        b-=1
        t+=count*2
        count+=1
    else:
        t+=count
        b=a
print(t)






