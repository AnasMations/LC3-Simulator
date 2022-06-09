#TODO fill all LC3 commands with their prespective binary
instrBinary = {
    "ADD":"1110",
    "AND":"0000"}

#We have 8 registers
R = [0, 0, 0, 0, 0, 0, 0, 0]
reg = {"R0":R[0], "R1":R[1], "R2":R[2], "R3":R[3], "R4":R[4], "R5":R[5], "R6":R[6], "R7":R[7]}

def decode(line):
    return line.replace(",", "").upper().split()

def machineCode(list):
    list = decode(list)
    binary = ""
    for i in list:
        if i in instrBinary:
            binary = binary + instrBinary[i]

    return  binary

#TODO simulate one line
def simulateLine(list):
    list = decode(list)


s = input("line: ")
print(machineCode(s))