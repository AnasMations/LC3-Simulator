# TODO
# ADD done
# AND done
# NOT done
# BRZ
# BRP
# BRN
# JMP
# LD
# ST

# TODO fill all LC3 commands with their prespective binary
# Equivalent binary code of each instruction
instrBinary = {
    "ADD": "1110",
    "AND": "0000"}

# We have 8 registers
REG = {"R0": 0, "R1": 0, "R2": 0, "R3": 0, "R4": 0, "R5": 0, "R6": 0, "R7": 0}

# Program counter
PC = 0

# file path that contains assembly code
FILEPATH = "test.txt"


def decode(line):
    return line.replace(",", "").replace("\n", "").upper().split()

# TODO print error messages if input isn't correct
def errorHandling(list):
    list = decode(list)

# TODO save converted binary code in a separate txt file
def machineCode(list):
    list = decode(list)
    binary = ""
    for instr in list:
        if instr in instrBinary:
            binary = binary + instrBinary[instr]

    return binary


def simulate(list):
    list = decode(list)
    print(list)
    global PC
    PC += 1
    for instr in list:
        if instr == "ADD":
            if list[3][0] == "#":
                REG[list[1]] = REG[list[2]] + int(list[3][1:])
            else:
                REG[list[1]] = REG[list[2]] + REG[list[3]]

        elif instr == "AND":
            if list[3][0] == "#":
                REG[list[1]] = REG[list[2]] & int(list[3][1:])
            else:
                REG[list[1]] = REG[list[2]] & REG[list[3]]

        elif instr == "NOT":
            if list[2][0] == "#":
                REG[list[1]] = ~int(list[2][1:])
            else:
                REG[list[1]] = ~REG[list[2]]


def simulateAll(lines):
    for line in lines:
        simulate(line)


def printSimulation():
    for k, v in REG.items():
        print(k+":\t"+str(v))
    print("PC:\t"+str(PC))


def openFileToList():
    FILE = open(FILEPATH, "r")
    lines = FILE.readlines()
    lines = [line.rstrip() for line in lines]
    return lines



#print(machineCode(s))
simulateAll(openFileToList())
printSimulation()
