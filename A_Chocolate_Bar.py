t=int(input())

for _ in range(t):

    n,l,r,k=list(map(int,input().split()))

    nums=list(map(int,input().split()))

    nums.sort()

    i=0

    ans=0
    while i<len(nums):

        if nums[i]>k or nums[i]>r:
            break

        if nums[i]>=l and nums[i]<=r :
            ans+=1
            k-=nums[i]
        i+=1
    print(ans)

