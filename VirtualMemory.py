from VirtualAddress import VirtualAddress

class VirtualMemory:
    def __init__(self, B, path):
        self.disk = [[0] * 512 for i in range(B)]
        self.PM =[0] * 524288
        self.freeFrames = list(range(B, 1, -1))
        self.fillMemory(path)



    def fillMemory(self, input):

        with open(input, 'r') as file:
            lines = file.readlines()
            line1 = lines[0].split()
            line2 = lines[1].split()

            #process line 1
            for i in range(2, len(line1), 3):
                s = int(line1[i-2])
                z = int(line1[i-1])
                f = int(line1[i])

                self.PM[2 * s] = z
                self.PM[2 * s + 1] = f
                if f >= 0:
                    self.freeFrames.remove(f)
            #process line 2
            for i in range(2, len(line2), 3):
                s = int(line2[i - 2])
                p = int(line2[i - 1])
                f = int(line2[i])

                segment = self.PM[s*2 + 1]
                if segment < 0:
                    diskBlock = abs(segment)
                    self.disk[diskBlock][p] = f
                else:
                    self.PM[segment * 512 + p] = f
                if f >= 0:
                    self.freeFrames.remove(f)







    def readBlock(self, b:int, m:int)-> None:
        """
        copies a block from disk into a frame of physical memor
        :param b: disk block index
        :param m: starting address of PM frame
        """
        buf = self.disk[b]
        i = m
        for elem in buf:
            self.PM[i] = elem
            i += 1

    def writeBlock(self, b:int, m:int) -> None:
        """
        Copies PM frame to disk block
        :param b: disk block index
        :param m: PM frame starting address
        """
        buf = []
        j = m
        for i in range(512):
            buf.append(self.PM[j])
            j += 1

        self.disk[b] = buf

    def translate(self, va):
        breakdown = VirtualAddress(va)

        s = breakdown['s']
        p = breakdown['p']
        w = breakdown['w']
        pw = breakdown['pw']

        if pw >= self.PM[2*s]:
            raise Exception('Error: Va outside of segment boundary')

        pt = self.PM[2*s + 1]

        if pt >= 0:
            pg = self.PM[512 * pt + p]
        else:
            block = abs(pt)
            self.PM[2*s+1] = self.freeFrames.pop()
            self.readBlock(block, self.PM[2*s+1]*512)
            pg = self.PM[self.PM[2*s+1]* 512 + p]



        if pg >= 0:
            pa = pg * 512 + w
        elif pg < 0:
            allocatedFrame = self.freeFrames.pop()
            self.PM[512* pt + p] = allocatedFrame
            pa = allocatedFrame * 512 + w


        return pa



