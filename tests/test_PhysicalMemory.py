import unittest
from PhysicalMemory import PhysicalMemory


class MyTestCase(unittest.TestCase):
    def testInit(self):
        pm = PhysicalMemory("../init.txt")


        self.assertEqual(pm[12], 3000)
        self.assertEqual(pm[13], 4)
        self.assertEqual(pm[2053], 9)
if __name__ == '__main__':
    unittest.main()
