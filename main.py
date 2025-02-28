from VirtualMemory import VirtualMemory

initFile = "files/init-dp.txt"

vm = VirtualMemory(1024, initFile)

with open('files/input-dp.txt', 'r') as inFile, open('output-dp.txt', 'w') as outFile:
    for line in inFile:
        addresses = line.split()
        for add in addresses:
            try:
                outFile.write(str(vm.translate(int(add))) + " ")
            except:
                outFile.write("-1 ")

