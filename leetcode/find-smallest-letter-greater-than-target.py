class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        smallest=letters[-1]
        l=0
        r=len(letters)-1

        while l<=r:
            mid=l+(r-l)//2
            if target<letters[mid]:
                smallest=min(smallest,letters[mid])
                r=mid-1
            else:
                l=mid+1
        return smallest if target<smallest else letters[0]
        