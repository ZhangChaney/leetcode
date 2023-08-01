#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
给你一个升序排列的数组nums，请你原地删除重复出现的元素，使每个元素只出现一次 ，返回删除后数组的新长度。
元素的相对顺序应该保持一致。然后返回nums中唯一元素的个数。

考虑nums的唯一元素的数量为k，你需要做以下事情确保你的题解可以被通过：

更改数组nums，使nums的前k个元素包含唯一元素，并按照它们最初在nums中出现的顺序排列。
nums的其余元素与nums的大小不重要。
返回 k。

eg1:
    输入：nums = [1,1,2]
    输出：2, nums = [1,2,_]

eg2:
    输入：nums = [0,0,1,1,1,2,2,3,3,4]
    输出：5, nums = [0,1,2,3,4]
"""
from typing import Tuple


def solution(arr: list) -> tuple[list, int]:
    """
    快慢指针:
        快指针fast遍历数组，慢指针记录不相同的元素的存储位置。
        因为所给数组为有序数组，则只需要比较快指针元素和慢指针元素大小
            - arr[fast] > arr[slow], 不同的元素存储slow
            - 反之为相同元素继续遍历
    """
    slow, fast = 0, 1
    while fast < len(arr):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

        fast += 1

    return arr, slow


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    nums, k = solution(nums)
    print(nums, k)
