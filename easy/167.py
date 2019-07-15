'''

给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。


'''


from collections import defaultdict
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # temp_dict = defaultdict(int)
        # for index, num in enumerate(numbers):
        #     temp_dict[num] = index
        # for i in temp_dict:
        #     other = target - i
        #     if temp_dict[other] != 0:
        #         break
        # if i == other :

        numbers_1=set(numbers)
        for i in numbers_1:
            T = target - i
            if T in numbers_1:
                break
        index = numbers.index(i) + 1
        if i == T:
            numbers.remove(i)
            index_2 = numbers.index(T)+2
        else:
            index_2 = numbers.index(T)+1

        if index > index_2:
            return index, index_2
        else:
            return index_2, index

    def other_twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        setnumbers = set()
        for i in range(len(numbers)):
            if numbers[i] in setnumbers:
                continue
            else:
                setnumbers.add(numbers[i])
            num = target - numbers[i]
            if num in numbers[i + 1:]:
                j = numbers[i + 1:].index(num)
                return [i + 1, i + j + 2]
        return None


a=Solution()
print(a.twoSum([0,0,3,4],0 ))