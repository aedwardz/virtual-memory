import unittest
from VirtualMemory import VirtualMemory


class MyTestCase(unittest.TestCase):

    def testFillMemory(self):
        vm = VirtualMemory(1024, '../testInit.txt')

        pmValues = {16: 4000,
                    17: 3,
                    18: 5000,
                    19: -7,
                    1536: 10,
                    1537: -20
                    }

        diskValues = {0: 13,
                      1: -25}

        for key, val in pmValues.items():
            self.assertEqual(vm.PM[key], val)

        for key, val in diskValues.items():
            self.assertEqual(vm.disk[7][key], val)

    def testLargePw(self):
        vm = VirtualMemory(1024, '../testInit.txt')
        va = 1575864
        with self.assertRaises(Exception):
            vm.translate(va)
    def testLargePw2(self):
        vm = VirtualMemory(1024, '../files/init-no-dp.txt')
        va = 524287
        vm.translate(va)

    def testTranslateDefault(self):
        vm = VirtualMemory(1024, '../testInit.txt')
        va = 2097162

        result = vm.translate(va)

        self.assertEquals(result, 5130)

    def testTranslateNonResidentPg(self):
        vm = VirtualMemory(1024, '../testInit.txt')
        va = 2097674

        vm.freeFrames.remove(2)
        result = vm.translate(va)

        self.assertEquals(result, 2058)

    def testTranslateNonResidentPt(self):
        vm = VirtualMemory(1024, '../testInit.txt')
        va = 2359306

        vm.freeFrames.remove(2)
        vm.freeFrames.remove(4)
        result = vm.translate(va)

        self.assertEquals(result, 6666)
    def testTranslateNonResidentPtPg(self):
        vm = VirtualMemory(1024, '../testInit.txt')
        va = 2359818

        vm.freeFrames = [14, 5]

        result = vm.translate(va)

        self.assertEquals(result, 7178)

    def testFinalTranslation(self):
        expected = [5130, 1034, 6666, 2570]
        inputs = [2097162, 2097674, 2359306, 2359818]
        result = []
        vm = VirtualMemory(1024, '../testInit.txt')

        for inp in inputs:
            result.append(vm.translate(inp))

        self.assertEquals(result, expected)



    def setUp(self):
        self.path = "../init.txt"
        self.vm = VirtualMemory(1024, self.path)
    def testWriteBlock(self):
        m = 0
        b = 3
        k = m
        for i in range(512):
            self.vm.PM[k] = 1
            k += 1

        self.vm.writeBlock(b, m)


        self.assertEqual(self.vm.disk[b], [1]* 512)



    def testReadBlock(self):

        b = 3
        m = 1

        self.vm.disk[b] = [1,2,3,4,5, 6, 7, 8, 9, 10,11,12,13]
        self.vm.readBlock(b, m)
        self.assertEqual(self.vm.PM[m: 1+len(self.vm.disk[b])], [1,2,3,4,5, 6, 7, 8, 9, 10,11,12,13])

        b = 2
        m = 378
        self.vm.disk[b] = [7] * 512
        self.vm.readBlock(b, m)
        self.assertEqual(self.vm.PM[m: m + len(self.vm.disk[b])], self.vm.disk[b])

    def testKc(self):
        vm = VirtualMemory(1024,"C:\\Users\\Antonio\\virtualMemory\\kc.txt")
        try:
            print(vm.translate(24))
            print(vm.translate(512))

        except:
            print('error')

        print(vm.translate(2098193))



if __name__ == '__main__':
    unittest.main()
