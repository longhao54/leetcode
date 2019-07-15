def bubble_sort_simple(list):
    """
    最简单的交换排序，时间复杂度O(n^2)
    """
    lis = list
    length = len(list)
    for i in range(length):
        for j in range(i + 1, length):
            if lis[i] > lis[j]:
                # print(lis[i])
                lis[i],lis[j] = lis[j], lis[i]
                print(lis)
        print("===")

myList = [49,38,65,97,76,13,27,49]
bubble_sort_simple(myList)


