## 题目描述
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和
为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序
列? Good Luck!

## 解题思路
双指针思路，初始值为1和2，然后在此基础上进行叠加，例如加3、4、5...以此类推。如果和为S则进行记录，如果大于S，则左端index减一，如果小于
S，则继续累加，知道累加数为S//2+1

## 时间复杂度
O(N)
