import unittest


# 这个count函数，可以正确返回字符数，字符数相等，输入是没字符的文件，输入是超大的文件，输入
from wc import count, count_lines


class TestCountlines(unittest.TestCase):
    def test(self):
        self.assertEqual(count_lines('test'), 3)

if __name__ == '__main__':
    unittest.main()

