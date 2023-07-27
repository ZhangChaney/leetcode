#!/usr/bin/python3
# -*- coding:utf-8 -*-
import time
from utils import timer
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


@timer
def solutionOne(arr: list) -> int:
    """
    暴力破解：
        1. 查找每个元素开始的长度为奇数的子数组
        2. 求和
        3. 时间复杂度O(n^3), 二重循环n方，其中求和函数等价于遍历一遍子序列，复杂度为n
    """
    ans = 0
    lens = len(arr)

    for i in range(lens):
        step = 1
        while i + step <= lens:
            temp = arr[i: i + step]
            ans += sum(temp)
            step += 2
    print(f'answer:  {ans}')

    return ans


@timer
def solutionTwo(arr: list) -> int:
    """
    前缀和：
        1. 计算前缀和数组prefixSum, 其中p[0] = 0, p[i] = sum(arr[: i + 1])从头到i的和
        2. 初始步长为step1， 遍历前缀和数组求和，遍历一遍后步长 + 2。
            - arr[i] = p[i + 1] - p[i]
            - arr[i: i + step] = p[i + step] - p[i]
        3. 时间复杂度O（n^2），求和O(n)独立出循环外，双层控制循环O(n^2)，实际时间复杂O（n^2 + n）
    """
    ans = 0
    lens = len(arr)
    prefixSum = [0] * (lens + 1)

    # 求前缀和数组
    for i in range(lens):
        prefixSum[i + 1] = prefixSum[i] + arr[i]

    # 遍历求和
    for i in range(lens + 1):
        step = 1
        while i + step <= lens:
            ans += (prefixSum[i + step] - prefixSum[i])
            step += 2

    print(f'answer:  {ans}')
    return ans


@timer
def solutionThree(arr: list) -> int:
    """
    数学：
        计算每个元素出现的次数求和，利用第i-1个元素出现的次数求得第i个元素出现的次数(动态规划思想)
        1. 第一个元素出现的次数固定为 len + 1 // 2, 记p(0)
        2. 第二个元素出现的次数为：
            - 第一个元素出现的次数
            - 减去仅有第一个元素出现，没有第二个元素出现的次数（i + 1 // 2）
            - 加上第二个元素出现但第第一元素未出现的次数(len - i + 1 // 2)
        3. 得到递推公式p(i) = p(0) - (i + 1 // 2) + (len - i + 1 // 2)
        4. 根据以上公式求得所有元素出现的次数，最后求和
        5. 复杂度O（n）， 2次单层遍历0(n + n)
    """
    ans = 0
    lens = len(arr)
    occurs = [0] * lens  # 数组记录每个元素出现的次数
    occurs[0] = (lens + 1) // 2  # arr[0] 出现的次数
    for i in range(1, lens):
        occurs[i] = occurs[i - 1] + ((lens - i + 1) // 2) - ((i + 1) // 2)

    for i in range(lens):
        # 总和等于累加（所有元素*该元素出现次数）
        ans += (arr[i] * occurs[i])

    print(f'answer:  {ans}')
    return ans


if __name__ == '__main__':
    data = list(range(3000))
    solutionOne(data)  # 19.92s
    solutionTwo(data)  # 0.399s
    solutionThree(data)  # 0.0001s
