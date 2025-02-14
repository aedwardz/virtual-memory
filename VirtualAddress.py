class VirtualAddress:
    MASK = 0x1FF
    MASK2 = 0x3FFF
    def __init__(self, VA):
        self.intAddress = VA
        self.VA = {
            "va": int(bin(VA), 2)

        }
        self.decompose()

    def __getitem__(self, item):
        return self.VA[item]


    def decompose(self):
        self.VA['s'] = self['va'] >> 18
        self.VA['p'] = (self['va'] >> 9) & self.MASK
        self.VA['w'] = self['va'] & self.MASK
        self.VA['pw'] = self['va'] & self.MASK2


