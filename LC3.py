#TODO fill all LC3 commands with their prespective binary
instrBinary = {
    "ADD":"1110",
    "AND":"0000"}

#We have 8 registers
reg = {"R0":0, "R1":0, "R2":0, "R3":0, "R4":0, "R5":0, "R6":0, "R7":0}

def decode(line):
    return line.replace(",", "").upper().split()

#TODO print error messages if input isn't correct
def errorHandling(list):
    list = decode(list)

def machineCode(list):
    list = decode(list)
    binary = ""
    for instr in list:
        if instr in instrBinary:
            binary = binary + instrBinary[instr]

    return  binary

def simulate(list):
    list = decode(list)
    for instr in list:
        if instr == "ADD":
            if list[3][0] == "#":
                reg[list[1]] = reg[list[2]] + int(list[3][1:])
            else:
                reg[list[1]] = reg[list[2]] + reg[list[3]]

def printSimulation():
    for k, v in reg.items():
        print(k, v)

#TODO simulate one line
def simulateLine(list):
    list = decode(list)


s = input("line: ")
print(machineCode(s))
simulate(s)
printSimulation()