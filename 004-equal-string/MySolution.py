class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1_part = [[s1[0], s1[2]], [s1[1], s1[3]]]
        s2_part = [[s2[0], s2[2]], [s2[1], s2[3]]]
        for i in range(len(s1_part)):
            s1_part[i].sort()
            s2_part[i].sort()
        if s1_part[0] == s2_part[0] and s1_part[1] == s2_part[1]:
            return True
        else:
            return False

s1 = 'abcd'
s2 = 'cdab'
s = Solution()
if s.canBeEqual(s1, s2):
    print('true')
else:
    print('false')