class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n=len(image[0])
        dic={0:1,1:0}
        
        for i in range(n):
            l=0
            r=n-1
            while l<=r:
                if image[i][l]==image[i][r]:
                    image[i][l],image[i][r]=dic[image[i][l]],dic[image[i][r]]
                l+=1
                r-=1
        return image


            

        