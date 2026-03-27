from idlelib.debugobj_r import remote_object_tree_item


class Solution(object):
    # 两个单条分割处理
    def canTwoSinglePartition(self, Grid1, Grid2):
        #print(1)
        if sum(Grid1) == sum(Grid2):
            return True
        elif sum(Grid1) > sum(Grid2):
            delta = sum(Grid1) - sum(Grid2)
            if (delta == Grid1[0] or delta == Grid1[-1]) and len(Grid1) > 1:
                return True
            else:
                return False
        else:
            delta = sum(Grid2) - sum(Grid1)
            if (delta == Grid2[0] or delta == Grid2[-1]) and len(Grid2) > 1:
                return True
            else:
                return False

    # 两行
    def isTwoRowPartition(self, grid):
        if len(grid) == 2:
            Grid1 = grid[0]
            Grid2 = grid[1]
            return self.canTwoSinglePartition(Grid1, Grid2)
        else:
            return False

    # 两列
    def isTwoColPartition(self, grid):
        if len(grid[0]) == 2:
            Grid1 = []
            Grid2 = []
            for row in grid:
                Grid1.append(row[0])
                Grid2.append(row[1])
            return self.canTwoSinglePartition(Grid1, Grid2)
        else:
            return False

    # 单对多分割情况处理
    def canOneAndMorePartition(self, RowGrid1, RowGrid2):
        if sum(RowGrid1) == sum(RowGrid2):
            return True
        elif sum(RowGrid1) > sum(RowGrid2):
            delta = sum(RowGrid1) - sum(RowGrid2)
            if delta == RowGrid1[0] or delta == RowGrid1[-1]:
                return True
            else:
                return False
        else:
            delta = sum(RowGrid2) - sum(RowGrid1)
            if delta in RowGrid2:
                return True
            else:
                return False

    # 多对多分割情况处理
    def canMoreAndMorePartition(self, Grid1, Grid2):
        if sum(Grid1) == sum(Grid2):
            return True
        elif sum(Grid1) > sum(Grid2):
            delta = sum(Grid1) - sum(Grid2)
            if delta in Grid1:
                return True
            else:
                return False
        else:
            delta = sum(Grid2) - sum(Grid1)
            if delta in Grid2:
                return True
            else:
                return False

    # 单行
    def isSingleRowPartition(self, grid):
        if len(grid) == 1:
            for i in range(1, len(grid[0])):
                Grid1 = []
                Grid2 = []
                for col in range(len(grid[0])):
                    if col < i:
                        Grid1.append(grid[0][col])
                    else:
                        Grid2.append(grid[0][col])
                #print(Grid1, Grid2)
                if self.canTwoSinglePartition(Grid1, Grid2):
                    return True
        else:
            return False

    # 单列
    def isSingleColPartition(self, grid):
        if len(grid[0]) == 1:
            for i in range(1, len(grid)):
                Grid1 = []
                Grid2 = []
                for row in range(len(grid)):
                    if row < i:
                        Grid1.append(grid[row][0])
                    else:
                        Grid2.append(grid[row][0])
                if self.canTwoSinglePartition(Grid1, Grid2):
                    return True
        else:
            return False

    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        # 单行情况
        if self.isSingleRowPartition(grid):
            #print(1)
            return True
        # 单列情况
        if self.isSingleColPartition(grid):
            return True
        # 两行情况
        if self.isTwoRowPartition(grid):
            #print('两行')
            return True
        # 两列情况
        if self.isTwoColPartition(grid):
            #print('两列')
            return True

        # 按行分割
        ## 单行处理
        if len(grid) > 2 and len(grid[0]) != 1:
            ### 首行
            RowGrid1 = grid[0]
            RowGrid2 = []
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if row != 0:
                        RowGrid2.append(grid[row][col])
            if self.canOneAndMorePartition(RowGrid1, RowGrid2):
                #print("首行")
                return True
            ### 末行
            RowGrid1 = grid[-1]
            RowGrid2 = []
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if row != len(grid) - 1:
                        RowGrid2.append(grid[row][col])
            if self.canOneAndMorePartition(RowGrid1, RowGrid2):
                #print("末行")
                return True
            ## 非单行处理
            for row_line in range(2, len(grid) - 1):
                Grid1 = []
                Grid2 = []
                for row in range(len(grid)):
                    for col in range(len(grid[0])):
                        if row < row_line:
                            Grid1.append(grid[row][col])
                        else:
                            Grid2.append(grid[row][col])
                #print(Grid1, Grid2)
                if self.canMoreAndMorePartition(Grid1, Grid2):
                    #print("行")
                    return True
        # 按列分割
        if len(grid[0]) > 2 and len(grid) != 1:
            ## 单列处理
            ### 首列
            ColGrid1 = []
            ColGrid2 = []
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if col == 0:
                        ColGrid1.append(grid[row][col])
                    else:
                        ColGrid2.append(grid[row][col])
            if self.canOneAndMorePartition(ColGrid1, ColGrid2):
                #print("首列")
                return True
            ### 末列
            ColGrid1 = []
            ColGrid2 = []
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if col == len(grid[0]) - 1:
                        ColGrid1.append(grid[row][col])
                    else:
                        ColGrid2.append(grid[row][col])
            if self.canOneAndMorePartition(ColGrid1, ColGrid2):
                #print("末列")
                return True
            ## 非单列处理
            for col_line in range(2, len(grid[0]) - 1):
                Grid1 = []
                Grid2 = []
                for row in range(len(grid)):
                    for col in range(len(grid[0])):
                        if col < col_line:
                            Grid1.append(grid[row][col])
                        else:
                            Grid2.append(grid[row][col])
                if self.canMoreAndMorePartition(Grid1, Grid2):
                    #print("列")
                    return True
        return False

grid = eval(input('Enter a m*n grid:'))   # [[1,2], [3,4]]
solution = Solution()
if solution.canPartitionGrid(grid):
    print("true")
else:
    print("false")