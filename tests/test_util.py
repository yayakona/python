# coding: UTF-8

import unittest
from srcs import util


class TestCommon(unittest.TestCase):


    def test_get_type_name(self):
       self.assertEqual(common.get_type_name(1), 'int')
       self.assertEqual(common.get_type_name("aa"), 'string')
       self.assertEqual(common.get_type_name([1,2]), 'list')


if __name__ == "__main__":
    unittest.main()