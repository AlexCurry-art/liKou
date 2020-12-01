# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 14:12
# @Author  : Alex
"""
判断字符串的排列是否在另一个字符串里面

思路：实际是考察字符串的所有排列组合
     采用递归的方式解决问题
"""


def get_all(list_a: list):
    """返回字符串a的所有排列组合"""
    for i in range(len(list_a)):
        str_t = list_a[i]
        array_t = list_a[0:i] + list_a[i + 1:]
        if len(array_t) > 1:
            for str_a in get_all(list_a[0:i] + list_a[i + 1:]):
                yield str_t + str_a
        else:
            yield str_t + array_t[0]


if __name__ == '__main__':
    results = list(set(get_all(list("abb"))))
    print(results)
