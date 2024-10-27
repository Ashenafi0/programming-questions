class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2):return False
        sh1={char: 0 for char in 'abcdefghijklmnopqrstuvwxyz'}
        sh2={char: 0 for char in 'abcdefghijklmnopqrstuvwxyz'}
        for char in s1:
            sh1[char]+=1
        for char in s2[:len(s1)]:
            sh2[char]+=1
        match=0
        for char in 'abcdefghijklmnopqrstuvwxyz':
            match+=(1 if sh1[char]==sh2[char] else 0)
        l=0
        for r in range(len(s1),len(s2)):
            if match==26: return True
            sh2[s2[r]]+=1
            if sh2[s2[r]]==sh1[s2[r]]:
                match+=1
            elif sh2[s2[r]]==sh1[s2[r]]+1:
                match-=1

            sh2[s2[l]]-=1
            if sh2[s2[l]]==sh1[s2[l]]:
                match+=1
            elif sh2[s2[l]]==sh1[s2[l]]-1:
                match-=1
            l+=1
        return match==26
            

     
       










