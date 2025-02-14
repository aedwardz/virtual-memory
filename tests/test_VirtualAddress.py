import unittest
from VirtualAddress import VirtualAddress


class MyTestCase(unittest.TestCase):
    def testVirtualAddress(self):
        va = VirtualAddress(789002)

        self.assertEqual(va['va'], int(bin(789002), 2))
        self.assertEqual(va['s'], 3)
        self.assertEqual(va['p'], 5)
        self.assertEqual(va['w'], 10)

    def testVirtualAddress2(self):
        va = VirtualAddress(1575424)

        self.assertEqual(va['va'], int(bin(1575424), 2))
        self.assertEqual(va['s'], 6)
        self.assertEqual(va['p'], 5)
        self.assertEqual(va['w'], 0)
        self.assertEqual(va['pw'], 2560)

    def testVirtualAddress3(self):
        va = VirtualAddress(1575863)

        self.assertEqual(va['va'], int(bin(1575863), 2))
        self.assertEqual(va['s'], 6)
        self.assertEqual(va['p'], 5)
        self.assertEqual(va['w'], 439)
        self.assertEqual(va['pw'], 2999)



if __name__ == '__main__':
    unittest.main()
