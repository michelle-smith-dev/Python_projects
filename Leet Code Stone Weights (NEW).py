# class Solution:
#     def lastStoneWeight(self, stones: list[int]) -> int:
#         # while true, repeat the process the length of the stones list
#         while stones:
#             # keep list sorted
#             stones.sort()
#             print(stones)
#             # assign last index value (-1) to a variable to store it by using the pop() method
#             max_val1 = stones.pop(-1)
#             if not stones:
#                 return max_val1
#             max_val2 = stones.pop(-1)
#             # subtract largest value from smaller value and append
#             # or determine if values are equal
#             if max_val1 > max_val2:
#                 i = max_val1 - max_val2
#                 stones.append(i)
#                 print(max_val1, "minus", max_val2, stones)
#             else:
#                 print("Both", max_val1, "and", max_val2, "are destroyed")
#         return 0
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:

        while len(stones) > 1:
            stones.sort()
            print(stones)
            maxval1 = stones.pop(-1)
            maxval2 = stones.pop(-1)
            if maxval1 > maxval2:
                i = maxval1 - maxval2
                stones.append(i)
                print(maxval1, "minus", maxval2, stones)
            else:  # for debug only
                print("Both", maxval1, "and", maxval2, "are destroyed")
        if len(stones) > 0:
            return stones[0]
        else:
            return 0


# stoneslist = [4, 43, 8, 65, 11, 2, 5, 10, 220]
stoneslist = [48, 3.24, 4.5, 88.72, 11, 6.98]
my_class = Solution()
my_class.lastStoneWeight(stoneslist)

# test_cases = [
#         ([1], 1),
#         ([1, 1], 0),
#         ([2], 2)
# ]
#
# for test in test_cases:
#     input = test[0]
#     expected = test[1]
#     my_class = Solution()
#     print('test:', test)
#     try:
#         actual = my_class.lastStoneWeight(input)
#         print('PASS')
#     except (Exception,):
#         print('FAIL')
#         print('more info here you may want')
#
# # if debug: print('stuff')
# # print("Expected:", expected)
# # print("actual:", actual)
#     assert actual == expected
