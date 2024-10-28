class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        ans=[]
        ans.append(celsius+273.15)
        ans.append(celsius*1.8+32)
        return ans
        