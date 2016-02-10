#!/usr/bin/env python
#encoding: utf-8


import unittest

global_coin = [1,3,5]

def DpFunc(inputNum):
    if inputNum == 0:
        return 0

    dpList = []

    for i in global_coin:
        if inputNum < i:
            continue
        else:
            dpList.append(DpFunc(inputNum - i) + 1)

    return min(dpList)



class DpTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Dp(self):
        self.assertEqual(0,DpFunc(0))
        self.assertEqual(1,DpFunc(1))
        self.assertEqual(2,DpFunc(2))
        self.assertEqual(1,DpFunc(3))
        self.assertEqual(1,DpFunc(5))
        self.assertEqual(3,DpFunc(11))
        self.assertEqual(4,DpFunc(12))

        

if __name__ == '__main__':
    unittest.main()
