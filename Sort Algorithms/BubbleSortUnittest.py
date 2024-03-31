import unittest
import BubbleSort


class MyTestCase(unittest.TestCase):
    def test_sorting(self):
        list1 = BubbleSort.bubble_sort([238, 89, 123, 0, 38, 99, 4])
        print("Testing test_sorting1")
        self.assertEqual(list1, [0, 4, 38, 89, 99, 123, 238])  # add assertion here

        list2 = BubbleSort.bubble_sort([4, 7, 0, 1, 1, 4, 0])
        print("Testing test_sorting2")
        self.assertEqual(list2, [0, 0, 1, 1, 4, 4, 7])


if __name__ == '__main__':
    unittest.main()
