#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import unittest
from operations.operations import sup

class Test(unittest.TestCase):
    def test_sup(self):
        res = sup(3, 1)
        self.assertTrue(res)