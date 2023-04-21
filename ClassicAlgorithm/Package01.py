from typing import List

"""
W: int, N: int, wt: List[int], val: List[int]
"""


def knapsack(W: int, N: int, wt: List[int], val: List[int]) -> int:
    # 初始化一个二维数组，用于存储状态
    # dp[i][w] 表示将前 i 个物品装入容量为 w 的背包中所获得的最大价值
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    # 开始进行递推
    for i in (1, N + 1):
        for w in (1, W + 1):
            # 当前商品 i 的重量小于等于当前容量 w，可以尝试将其放入背包中
            # 取最大值，考虑是将其放入之前的最优方案中还是选择不放
            if w - wt[i] < 0:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(
                    # 不把物品 i 装进背包
                    dp[i - 1][w],
                    # 把物品 i 装进背包
                    dp[i - 1][w - wt[i]] + val[i]
                )
    # 返回最大价值
    return dp[N][W]
