## 题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

## 解题思路
1. 负数转为补码，即n&0xffffffff(32位)
2. 使用位操作，n & (n-1)即可将二进制最末尾的1变成0

## 时间复杂度
O(logn)
