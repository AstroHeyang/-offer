## 题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
注意：保证测试中不会当栈为空的时候，对栈调用pop()或者min()或者top()方法。

## 解题思路
额外创建最小栈，保证最小栈顶为最小值，具体操作如下：
当推入栈的数小于栈顶最小值，推入该数，否则推入栈顶最小值

## 时间复杂度
O(n)
