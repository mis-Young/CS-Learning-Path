class Solution:
    def areSimilar(self, mat, k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k %= n

        for i in range(m):
            for j in range(n):
                if mat[i][j] != mat[i][(j + k) % n]:
                    return False
        return True

#
# 作者：力扣官方题解
# 链接：https: // leetcode.cn / problems / matrix - similarity - after - cyclic - shifts / solutions / 3929537 / xun - huan - yi - wei - hou - de - ju - zhen - xiang - si - tta49 /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。