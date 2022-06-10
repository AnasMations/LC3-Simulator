# TODO
# ADD done
# AND done
# NOT done
# JMP done
# BRZ
# BRP
# BRN
# LD
# ST

class LC3:
    def __init__(self, FILEPATH):
        # TODO fill all LC3 commands with their prespective binary
        # Equivalent binary code of each instruction
        self.instrBinary = {
            "ADD": "1110",
            "AND": "0000"}

        # We have 8 registers
        self.REG = {"R0": 0, "R1": 0, "R2": 0, "R3": 0, "R4": 0, "R5": 0, "R6": 0, "R7": 0}

        # Program counter
        self.PC = 0

        # file path that contains assembly code
        self.FILEPATH = FILEPATH

        # instruction memory
        self.instrMemory = self.openFileToList()

    def decode(self, line):
        return line.replace(",", "").replace("\n", "").upper().split()

    # TODO print error messages if input isn't correct
    def errorHandling(self, list):
        list = self.decode(list)

    # TODO save converted binary code in a separate txt file
    def machineCode(self, list):
        binary = ""
        for instr in list:
            if instr in self.instrBinary:
                binary = binary + self.instrBinary[instr]

        return binary

    def simulate(self):
        list = self.instrMemory[self.PC]
        for instr in list:
            if instr == "ADD":
                if list[3][0] == "#":
                    self.REG[list[1]] = self.REG[list[2]] + int(list[3][1:])
                else:
                    self.REG[list[1]] = self.REG[list[2]] + self.REG[list[3]]

            elif instr == "AND":
                if list[3][0] == "#":
                    self.REG[list[1]] = self.REG[list[2]] & int(list[3][1:])
                else:
                    self.REG[list[1]] = self.REG[list[2]] & self.REG[list[3]]

            elif instr == "NOT":
                if list[2][0] == "#":
                    self.REG[list[1]] = ~int(list[2][1:])
                else:
                    self.REG[list[1]] = ~self.REG[list[2]]

            elif instr == "JMP":
                for i in range(0, len(self.instrMemory)):
                    if list[1] == self.instrMemory[i][0]:
                        self.PC = i + 1
                        return
        self.PC += 1


    def simulateAll(self):
        while(self.instrMemory[self.PC][0] != ".END"):
            print(self.instrMemory[self.PC])
            self.simulate()


    def printSimulation(self):
        for k, v in self.REG.items():
            print(k+":\t"+str(v))
        print("PC:\t"+str(self.PC))


    def openFileToList(self):
        FILE = open(self.FILEPATH, "r")
        lines = FILE.readlines()
        lines = [line.rstrip() for line in lines]
        for i in range(0, len(lines)):
            lines[i] = self.decode(lines[i])
        return lines


test = LC3("test.txt")
test.simulateAll()
test.printSimulation()
