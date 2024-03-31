import unittest
import ImplementQueueWithStacks
from ImplementQueueWithStacks import MyQueue


class Queue(unittest.TestCase):
    def test_stacks(self):

        self.assertEqual(push(31), [31])  # add assertion here


if __name__ == '__main__':
    unittest.main()
