import copy

class Solution:
    def OddRow(self, mat):
        m = len(mat)
        n = len(mat[0])
        for row in range(m):
            if row % 2 == 0:
                temp = mat[row][-1]
                for col in range(n - 1, 0, -1):
                    mat[row][col] = mat[row][col-1]
                mat[row][0] = temp
        return mat

    def EvenRow(self, mat):
        m = len(mat)
        n = len(mat[0])
        for row in range(m):
            if row % 2 == 1:
                temp = mat[row][0]
                for col in range(0, n - 1):
                    mat[row][col] = mat[row][col+1]
                mat[row][-1] = temp
        return mat

    def areSimilar(self, mat, k: int) -> bool:
        InitialMat = copy.deepcopy(mat)
        for _ in range(k):
            mat = self.OddRow(mat)
            mat = self.EvenRow(mat)
            print(mat)
        if InitialMat == mat:
            return True
        else:
            return False

mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]]
if Solution().areSimilar(mat, 2):
    print("yes")
else:
    print("no")