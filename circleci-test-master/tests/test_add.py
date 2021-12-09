#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import unittest
from operations.operations import add

class Test(unittest.TestCase):
    def test_add(self):
        res = add(1, 2)
        self.assertEqual(res, 3)