class PhysicalMemory:
    def __init__(self, input):
        self.PM = [0] * 524288
        self.fillMemory(input)
    def __getitem__(self, item):
        return self.PM[item]
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
            #process line 2
            for i in range(2, len(line2), 3):
                s = int(line2[i - 2])
                p = int(line2[i - 1])
                f = int(line2[i])

                self.PM[self.PM[2*s+1] * 512 + p] = f
