
class Solution:
    def findLcp(self, Str_List, n):
        lcp = [[0 for _ in range(n)] for _ in range(n)]
        # 从后往前生成lcp
        for i in range (n - 1, -1, -1):
            for j in range (n - 1, -1, -1):
                if Str_List[i] == Str_List[j]:
                    if i == n - 1 or j == n - 1:
                        lcp[i][j] = 1
                    else:
                        lcp[i][j] = lcp[i + 1][j + 1] + 1
        return lcp


    def findTheString(self, lcp):
        n = len(lcp)
        letters = 'abcdefghijklmnopqrstuvwxyz'
        Str_List = [-1 for _ in range(n)]
        char = 0
        # 判断字符串要相等的部分
        for i in range(n):
            for j in range(n):
                # 先将所有a找出来
                if i == 0:
                    if lcp[i][j] != 0:
                        Str_List[j] = 0
                if i != j:
                    # 若未被分配过，直接分配最小的字母给这一个位置
                    if Str_List[i] == -1:
                        char += 1
                        Str_List[i] = char
                    # 若lcp中两个字符串有重复元素，则str中第i和第j为应该为什么相同字母
                    if lcp[i][j] != 0:
                        Str_List[j] = Str_List[i]
        # 若要生成的字母超过26个，则直接返回空串
        if max(Str_List) > 25:
            return ''
        # 根据规则生成str
        str = ''
        for i in range(n):
            str += letters[Str_List[i]]
        # 根据Str_List生成对应的lcb
        lcp2 = self.findLcp(Str_List, n)
        print(lcp2)
        print(Str_List)
        if lcp == lcp2:
            return str
        else:
            return ''

lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
s = Solution()
print(s.findTheString(lcp))

