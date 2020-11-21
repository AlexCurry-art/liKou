# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 14:12
# @Author  : Alex
"""
所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。



示例 1：

输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC","CCCCCAAAAA"]
示例 2：

输入：s = "AAAAAAAAAAAAA"
输出：["AAAAAAAAAA"]


提示：

0 <= s.length <= 105
s[i] 为 'A'、'C'、'G' 或 'T'
"""


def findRepeatedDnaSequences(s: str) -> list:
    """时间复杂度 O(N)"""
    r, rt = set(), set()
    for i in range(len(s) - 10 + 1):
        t = s[i:i + 10]
        if t in r:
            rt.add(t)
        r.add(t)
    return list(rt)


if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    result = findRepeatedDnaSequences(s)
    print(result)
