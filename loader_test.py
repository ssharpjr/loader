#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import loader

class TestLoader(unittest.TestCase):
    def setUp(self):
        self.get_wo_scan = loader.get_wo_scan()

    def test_get_wo_scan_returns_correct_type(self):
        # self.assertEquals() something here

if __name__ == '__main__':
    unittest.main()

