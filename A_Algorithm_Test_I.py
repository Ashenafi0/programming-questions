n=int(input())

nums=list(map(int,input().split()))

num=len(set(nums))
seq=1

while num!=0:
    seq*=num
    num-=1
print(seq)
