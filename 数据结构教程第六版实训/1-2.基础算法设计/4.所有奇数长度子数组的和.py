#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。

子数组 定义为原数组中的一个连续子序列。

请你返回 arr 中 所有奇数长度子数组的和 。

eg1:
    输入：arr = [1,4,2,5,3]
    输出：58
    解释：所有奇数长度子数组和它们的和为：
            [1] = 1
            [4] = 4
            [2] = 2
            [5] = 5
            [3] = 3
            [1,4,2] = 7
            [4,2,5] = 11
            [2,5,3] = 10
            [1,4,2,5,3] = 15
    我们将所有值求和得到 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

eg2:
    输入：arr = [1,2]
    输出：3
    解释：总共只有 2 个长度为奇数的子数组，[1] 和 [2]。它们的和为 3 。
"""


def solutionOne(arr: list) -> int:
    """
        1. 查找每个元素开始的长度为奇数的子数组
        2. 求和
    """
    ans = 0
    lens = len(arr)

    for i in range(lens):
        step = 1
        while i + step <= lens:
            temp = arr[i: i + step]
            ans += sum(temp)
            step += 2
    print(ans)

    return ans


if __name__ == '__main__':
    arr = [1, 4, 2, 5, 3]
    solutionOne(arr)
