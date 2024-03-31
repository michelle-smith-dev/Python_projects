"""Binary Search looks the mid-point of a sorted list, if the number is the target, it stops searching.
sudo code:

first get sorted array
identify target number (input?)
get mid-point of array
if target is mid-point, stop search.
if mid-point is less than target, we can drop index 0 - mid-point
if mid-point is larger than target, we can drop mid-point - index -1
Of the remaining array, find new mid-point and repeat until target is found."""
debug = True

class BinarySearch:

    def __init__(self, val, target):
        self.val = val
        self.target = target
        print("List:", self.val, "\nTarget:", self.target)

    def search(self):
        self.val.sort()
        mp = len(self.val) // 2

        left = self.val[0: mp]
        right = self.val[mp:]
        if debug: print("Mid-point:", mp, "\nLeft Side:", left, "\nRight Side:", right)
        if self.target == self.val[mp]:
            print("You found it!")
        elif self.target < self.val[mp]:
            new_list = BinarySearch(left, self.target)
            new_list.search()
        elif self.target > self.val[mp]:
            new_list = BinarySearch(right, self.target)
            new_list.search()


targ = int(input("What number do you want to find? "))
list1 = BinarySearch([88, 2, 4, 6, 8, 3], targ)
list1.search()
# BinarySearch.search(list1)