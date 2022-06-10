# TODO
# ADD done
# AND done
# NOT done
# JMP BR done
# BRZ done
# BRP BRPZ done
# BRN BRNZ done
# LD
# ST

class LC3:
    # initialize all the values
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

    # run only one step
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

            elif instr == "JMP" or instr == "BR":
                for i in range(0, len(self.instrMemory)):
                    if list[1] == self.instrMemory[i][0]:
                        self.PC = i + 1
                        return

            elif instr == "BRZ":
                if self.REG[ self.instrMemory[self.PC-1][1] ] == 0:
                    for i in range(0, len(self.instrMemory)):
                        if list[1] == self.instrMemory[i][0]:
                            self.PC = i + 1
                            return

            elif instr == "BRP":
                if self.REG[ self.instrMemory[self.PC-1][1] ] > 0:
                    for i in range(0, len(self.instrMemory)):
                        if list[1] == self.instrMemory[i][0]:
                            self.PC = i + 1
                            return

            elif instr == "BRN":
                if self.REG[ self.instrMemory[self.PC-1][1] ] < 0:
                    for i in range(0, len(self.instrMemory)):
                        if list[1] == self.instrMemory[i][0]:
                            self.PC = i + 1
                            return

            elif instr == "BRPZ":
                if self.REG[ self.instrMemory[self.PC-1][1] ] >= 0:
                    for i in range(0, len(self.instrMemory)):
                        if list[1] == self.instrMemory[i][0]:
                            self.PC = i + 1
                            return

            elif instr == "BRNZ":
                if self.REG[ self.instrMemory[self.PC-1][1] ] <= 0:
                    for i in range(0, len(self.instrMemory)):
                        if list[1] == self.instrMemory[i][0]:
                            self.PC = i + 1
                            return
        self.PC += 1

    # run all
    def simulateAll(self):
        while(self.instrMemory[self.PC][0] != ".END"):
            print(self.instrMemory[self.PC])
            self.simulate()

    # print all registers and their values along with the PC
    def printSimulation(self):
        for k, v in self.REG.items():
            print(k+":\t"+str(v))
        print("PC:\t"+str(self.PC))

    # convert string to list
    def decode(self, line):
        return line.replace(",", "").replace("\n", "").replace(":", "").upper().split()

    # read all the string lines in the txt file and convert them into list to get stored in instrMemory
    def openFileToList(self):
        FILE = open(self.FILEPATH, "r")
        lines = FILE.readlines()
        lines = [line.rstrip() for line in lines]
        instructions = []
        for i in range(0, len(lines)):
            if (lines[i].find(";") != -1):
                if (lines[i][0] == ";"):
                    continue
                else:
                    instructions.append( lines[i][:lines[i].find(";")] )
            elif (lines[i]==""):
                continue
            else:
                instructions.append(lines[i])

        for i in range(0, len(instructions)):
            instructions[i] = self.decode(instructions[i])

        return instructions
