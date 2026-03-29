from collections import Counter

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/check-if-strings-can-be-made-equal-with-operations-i/solutions/2424888/on-tong-yong-zuo-fa-pythonjavacgo-by-end-oj0d/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。