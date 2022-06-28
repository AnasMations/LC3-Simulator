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
    def __init__(self):
        # TODO fill all LC3 commands with their prespective binary
        # Equivalent binary code of each instruction
        self.instrBinary = {
            "ADD": "1110",
            "AND": "0000"}

        # We have 8 registers
        self.REG = {"R0": 0, "R1": 0, "R2": 0, "R3": 0, "R4": 0, "R5": 0, "R6": 0, "R7": 0}

        # Program counter
        self.PC = 0

        # instruction memory
        self.instrMemory = []

    # TODO print error messages if input isn't correct
    def errorHandling(self, list):
        list = self.decode(list)

    # TODO save converted binary code in a separate txt file
    # def machineCode(self, list):
    #     binary = ""
    #     for instr in list:
    #         if instr in self.instrBinary:
    #             binary = binary + self.instrBinary[instr]
    #
    #     return binary

    def Lc3ToMachine(self, Lc3Code):

        setOfRegisters = {'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7'}
        setOfNegativeNumbers = {'#-15', '#-14', '#-13', '#-12', '#-11', '#-10', '#-9', '#-8', '#-7', '#-6', '#-5',
                                '#-4', '#-3', '#-2', '#-1'}
        setOfNonNegativeNumbers = {'#15', '#14', '#13', '#12', '#11', '#10', '#9', '#8', '#7', '#6', '#5', '#4', '#3',
                                   '#2', '#1', '#0'}
        setOfnzp = {'N', 'Z', 'P', 'NZ', 'ZP', 'NP', 'NZP'}
        dictOfThreeBinaryDigits = {
            "0": "000",
            "1": "001",
            "2": "010",
            "3": "011",
            "4": "100",
            "5": "101",
            "6": "110",
            "7": "111"
        }

        dictOfFiveBinaryDigits = {
            "0": "00000", "1": "00001", "2": "00010", "3": "00011", "4": "00100",
            "5": "00101", "6": "00110", "7": "00111", "8": "01000", "9": "01001",
            "10": "01010", "11": "01011", "12": "01100", "13": "01101", "14": "01110", "15": "01111",

            "-1": "11111", "-2": "11110", "-3": "11101", "-4": "11100", "-5": "11011",
            "-6": "11010", "-7": "11001", "-8": "11000", "-9": "10111", "-10": "10110",
            "-11": "10101", "-12": "10100", "-13": "10011", "-14": "10010", "-15": "10001", "-16": "10000"
        }

        dictOfOpcodes = {
            "ADD": "0001",
            "AND": "0101",
            "NOT": "1001",
            "JMP": "1100",
            "BR": "0000",
            "JSR": "0100"
        }

        # Initialize machine code var with dump value in case of errors
        binaryCode = "0000000000000000"
        opcode = ""

        # ADD & AND operation
        if Lc3Code[0] == "ADD" or Lc3Code[0] == "AND":

            # assign opcode value
            opcode = dictOfOpcodes[Lc3Code[0]]

            ### Start handling errors

            # check if the length of the operation is not right --> 4
            if len(Lc3Code) != 4:
                print('The lenght is Wrong\n')
                return binaryCode

            # check if the registers not in the setOfRegisters
            if Lc3Code[1] not in setOfRegisters or Lc3Code[2] not in setOfRegisters:
                print('The registers location is incorrect\n')
                return binaryCode

            # check if the forth element not a register nor an immediate value
            if Lc3Code[3] not in setOfRegisters and Lc3Code[3] not in setOfNonNegativeNumbers and Lc3Code[
                3] not in setOfNegativeNumbers:
                print('The forth element has a problem\n')
                return binaryCode

                ### Finish handling errors

                ### Start returning machine code
            # check if the forth element is a register
            if Lc3Code[3] in setOfRegisters:
                DR = dictOfThreeBinaryDigits[Lc3Code[1][1]]
                SR1 = dictOfThreeBinaryDigits[Lc3Code[2][1]]
                SR2 = dictOfThreeBinaryDigits[Lc3Code[3][1]]
                binaryCode = opcode + DR + SR1 + "000" + SR2
                return binaryCode

            # if the forth element is an immediate value
            DR = dictOfThreeBinaryDigits[Lc3Code[1][1]]
            SR1 = dictOfThreeBinaryDigits[Lc3Code[2][1]]
            imm5 = dictOfFiveBinaryDigits[Lc3Code[3][1:]]
            binaryCode = opcode + DR + SR1 + "1" + imm5
            return binaryCode
            ### Finish returning machine code

        # NOT operation
        elif Lc3Code[0] == "NOT":
            # assign opcode value
            opcode = dictOfOpcodes[Lc3Code[0]]

            ### Start handling errors

            # check if the length of the operation is not right  --> 3
            if len(Lc3Code) != 3:
                print('The lenght is Wrong\n')
                return binaryCode

            # check if the registers not in the setOfRegisters
            if Lc3Code[1] not in setOfRegisters or Lc3Code[2] not in setOfRegisters:
                print('The registers location is incorrect\n')
                return binaryCode
                ### Finish handling errors

                ### Start returning machine code ###
            DR = dictOfThreeBinaryDigits[Lc3Code[1][1]]
            SR1 = dictOfThreeBinaryDigits[Lc3Code[2][1]]
            binaryCode = opcode + DR + SR1 + "111111"
            return binaryCode
            ### Finish returning machine code ###

        # BR operation
        elif Lc3Code[0][0:2] == "BR":
            # assign opcode value
            opcode = dictOfOpcodes[Lc3Code[0][0:2]]

            ### Start handling errors

            # check if the length of the operation is not right  --> 2
            if len(Lc3Code) != 2:
                print('The lenght is Wrong\n')
                return binaryCode

            # check the order of nzp
            if (Lc3Code[0][2:] not in setOfnzp):
                print('npz order is Wrong\n')
                return binaryCode
                ### Finish handling errors

                ### Start returning machine code ###
            offset = 4
            binaryOffset = self.decimalToBinary(offset, 9)
            n = '0';
            p = '0';
            z = '0';
            for x in Lc3Code[0]:
                if x == 'N':     n = '1'
                if x == 'P':     p = '1'
                if x == 'Z':     z = '1'

            binaryCode = opcode + n + z + p + binaryOffset
            return binaryCode
            ### Finish returning machine code ###

        # JMP operation
        elif Lc3Code[0] == 'JMP':
            # assign opcode value
            opcode = dictOfOpcodes[Lc3Code[0]]

            ### Start handling errors

            # check if the length of the operation is not right  --> 2
            if len(Lc3Code) != 2:
                print('The lenght is Wrong\n')
                return binaryCode

            # check the register is not in the setOfRegisters
            if (Lc3Code[1] not in setOfRegisters):
                print('the register is Wrong\n')
                return binaryCode
                ### Finish handling errors

                ### Start returning machine code ###
            baseR = dictOfThreeBinaryDigits[Lc3Code[1][1]]
            binaryCode = opcode + '000' + baseR + '000000'
            return binaryCode
            ### Finish returning machine code ###

        # JSR operation
        elif Lc3Code[0] == 'JSR':
            # assign opcode value
            opcode = dictOfOpcodes[Lc3Code[0]]

            ### Start handling errors

            # check if the length of the operation is not right  --> 2
            if len(Lc3Code) != 2:
                print('The lenght is Wrong\n')
                return binaryCode

                ### Finish handling errors

                ### Start returning machine code ###
            offset = self.calculateOffset(Lc3Code[1])
            binaryOffset = self.decimalToBinary(offset, 11)
            binaryCode = opcode + '1' + binaryOffset;
            return binaryCode
            ### Finish returning machine code ###
        return "0000000000000000"

    def decimalToBinary(self, n, binLen):
        binary = bin(n).replace("0b", "")
        while len(binary) != binLen:
            binary = '0' + binary
        return binary

    def calculateOffset(self, label):
        curr=-1
        jmp=-1
        c=0
        for i in range(0, len(self.instrMemory)):
            if len(self.instrMemory[i])<=1:
                c+=1
            if label == self.instrMemory[i][0]:
                jmp = i-c
            if len(self.instrMemory[i]) >= 2 and self.instrMemory[i][0]=="JMP" and self.instrMemory[i][1]==label:
                curr = i-c
            if curr!=-1 and jmp!=-1:
                break
        offset = (jmp - curr  - (jmp>curr) + (curr>jmp))-1
        return offset

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

            elif instr == "JSR" or instr == "BR":
                for i in range(0, len(self.instrMemory)):
                    if list[1] == self.instrMemory[i][0]:
                        self.PC = i + 1
                        return

            elif instr == "JMP":
                self.PC = self.REG[list[1]]
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
            elif instr == ".END":
                return
        self.PC += 1

    # run all
    def simulateAll(self):
        while(self.instrMemory[self.PC][0] != ".END"):
            # print(self.instrMemory[self.PC])
            self.simulate()

    def reset(self):
        self.PC = 0
        self.REG = {"R0": 0, "R1": 0, "R2": 0, "R3": 0, "R4": 0, "R5": 0, "R6": 0, "R7": 0}

    # print all registers and their values along with the PC
    def getAllRegisters(self):
        s = ""
        for k, v in self.REG.items():
            s += (k+":\t"+str(v)+"\n")
        s += ("\nPC:\t"+str(self.PC))
        return s

    def getInstructions(self):
        s = ""
        for i in range(0, self.PC):
            s += str(i) + "| " + str(self.instrMemory[i]) + "\n"
        return s.replace("'", "").replace(",", "")

    def getMahcinecode(self):
        s = ""
        for i in range(0, self.PC):
            s += self.Lc3ToMachine(self.instrMemory[i]) + "\n"
        print(s)
        return s

    # convert string to list
    def decode(self, line):
        return line.replace(",", "").replace("\n", "").replace(":", "").upper().split()

    # read all the string lines in the txt file and convert them into list to get stored in instrMemory
    def openFileToList(self, FILEPATH):
        FILE = open(FILEPATH, "r")
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

        self.instrMemory = instructions
        return instructions

    def readStringToList(self, s):
        lines = s.split("\n")
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

        self.instrMemory = instructions
        return instructions