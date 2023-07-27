#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
给你一个数组 nums和一个值 val，你需要 原地 移除所有数值等于val的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

eg:
    输入：nums = [3,2,2,3], val = 3
    输出：2, nums = [2,2]
    解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。
         例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。
"""


def solution(arr, target):
    """
        1. 定义头尾两个指针head, tail，从头指针遍历数组
        2. 如果arr[head] == target 且 arr[tail] != target, 两个元素互换位置
        3. 如果arr[tail] == target, 则tail - 1
    """
    head, tail = 0, len(arr) - 1
    while head <= tail:
        if arr[tail] == target:
            tail -= 1
            continue
        if arr[head] == target:
            arr[head], arr[tail] = arr[tail], arr[head]
        head += 1

    print(head, nums)
    return head


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    solution(nums, val)
