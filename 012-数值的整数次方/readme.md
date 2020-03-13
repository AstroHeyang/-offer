## 题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0

## 解题思路
二分法思路，求快速幂。递归法如下：如果指数为偶数，则返回power(base * base, exponent // 2);
如果为奇数，则返回power(base * base, exponent // 2) * base。
另外需要注意幂指数为负数的情况。

## 时间复杂度
O(log n)
