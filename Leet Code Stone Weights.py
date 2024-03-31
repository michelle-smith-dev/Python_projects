'''
[always increasing...]
minheap -> maxheap
[1, 1, 2, 3]

[-1, -1, -2, -3]

[-3, -2, -1, -1]

[-3, -1, 0, 2, 4]

get order, so that the largest are always to the right
use a pop method to get values you want

[1, 3, 2, 1]

[1, 1, 2, 3]
get max value: 3
create a list without max value1
[1, 1, 2]
get max value: 2
create a list without max value2

resulting list: [1, 1]
max value1 and value2: 3 2
larger minus smaller -> 3 - 2 -> 1
append 1 to resulting list: [1, 1, 1]
repeat
'''


# We will define the variable stones with our array of integers.
# Playing a game that has turns means we will use a for loop to loop over the array
# Create a function and pass the stone variable with our list; create an empty list to append our updated values to
# How do we find the max number in a list? Can use the max function possibly, but then how do I get the next highest value?
debug = False


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        assert type(stones) == list
        while len(stones) > 1:
            stones.sort()
            if debug: print(stones)
            maxval1 = stones.pop(-1)
            maxval2 = stones.pop(-1)
            if maxval1 > maxval2:
                i = maxval1 - maxval2
                stones.append(i)
                if debug: print(maxval1, "minus", maxval2, stones)
            else:  # for debug only
                if debug: print("Both", maxval1, "and", maxval2, "are destroyed")
        if len(stones) > 0:
            return stones[0]
        else:
            return 0


test_cases = [
        ([1], 1),
        ([1, 1], 0),
        ([2], 2),
        ([-33, 9, 0, 400, -24, 1002], 650),
        ('a', 'a'),
        (['a', 'b'], 'a', 'b'),
        ([3, 4], [5, 10], 1, 5),
        ([0], 0),
        ([4, 43, 8, 65, 11, 2, 5, 10], 0),
        ([4, 43, 8, 65, 11, 2, 5, 10, 220], 72),
        ([48, 3.24, 4.5, 88.72, 11, 6.98], 14.999999999999998),
        ([], []),
]

# Code doesn't test for correct input type, therefore test cases cannot test code for incorrect data
for test in test_cases:
    input = test[0]
    expected = test[1]
    my_class = Solution()
    print('test:', test)
    try:
        actual = my_class.lastStoneWeight(input)
        assert actual == expected
        print('PASS')
    except (Exception,):
        print('FAIL')

# if debug: print('stuff')
# print("Expected:", expected)
# print("actual:", actual)


# stoneslist = [4, 43, 8, 65, 11, 2, 5, 10, 58, 3]
# my_class = Solution()
# my_class.lastStoneWeight(stoneslist)

# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         max_stones1 = max(stones)
#         # then remove the max value from the list
#         # get the max value of the new list
#         # then remove this 2nd max value from the list
#         # compare max_stones1 to max_stones2, and get the new weight of the non-destroyed weight and append to list.
#         # repeat process until 1 stone remains, and then return the weight of last remaining stone
#         new_list = []
#         max_stones2 = max(new_list)
#         for i in stones:
#             if stones < max_stones1:
#                 new_list.append(stones)
#         return self.smash(max_stones1, max_stones2)
#
#     def smash(self, val1, val2):
#         if val1 > val2:
#             i = val1 - val2
#             new_list.append(i)
#         elif val2 > val1:
#             i = val2 - val1
#             new_list.append(i)
#         else:
#             print("Both stones are destroyed")
#         return compare(new_list)
#
#
# stones = [4, 43, 8, 65, 11, 2, 5, 10]
# lastStoneWeight(stones)