#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

eg1:
    输入：nums = [1,1,1,2,2,3]
    输出：5, nums = [1,1,2,2,3]

eg2:
    输入：nums = [0,0,1,1,1,1,2,3,3]
    输出：7, nums = [0,0,1,1,2,3,3]
"""


def solution(arr):
    """
    双指针
    :param arr:
    :return:
    """
    if len(arr) <= 2:
        return arr, len(arr)

    fast, slow = 2, 2
    while fast < len(arr):
        if arr[fast] != arr[slow - 2]:
            arr[slow] = arr[fast]
            slow += 1
        fast += 1

    return arr, slow


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    nums, k = solution(nums)
    print(nums[: k], k)
