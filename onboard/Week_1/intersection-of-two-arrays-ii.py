class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mylist=[]
        if len(nums1)<len(nums2):
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    nums2.remove(nums1[i])
                    mylist.append(nums1[i])
        else:
            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    nums1.remove(nums2[i])
                    mylist.append(nums2[i])
        return mylist


