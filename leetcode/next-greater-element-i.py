class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic=defaultdict(lambda:-1)
        stack=[]
        for i in range(len(nums2)):
            if stack:
                while stack and  stack[-1]<nums2[i]:
                    dic[stack.pop()]=nums2[i]
                stack.append(nums2[i])
            else:
                stack.append(nums2[i])
        output=[]
        for i in range(len(nums1)):
            output.append(dic[nums1[i]])
        return output



        