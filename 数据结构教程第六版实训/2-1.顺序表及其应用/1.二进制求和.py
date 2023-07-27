#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。

eg:
    输入:a = "11", b = "1"
    输出："100"
"""


def solution(a: str, b: str) -> str:
    ans = '{0:b}'.format(int(a, 2) + int(b, 2))

    print(ans)
    return ans


if __name__ == '__main__':
    x, y = '11', '1'
    solution(x, y)
