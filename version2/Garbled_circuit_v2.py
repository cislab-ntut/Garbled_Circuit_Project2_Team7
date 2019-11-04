#Garbled Circuit
#python3.6
#coding=utf-8

import random
import hashlib
import string

PLAINTEXT = ""

INPUT = []  #name of input line
OUTPUT = [] #name of output line
WIRE = []  #name of line
GARBLED_WIRE = dict()  #garbled name of line
CIRCUIT = dict()  #circuit description like verilog
GARBLED_TRUTH_TABLE = dict()  #garbled truth table

#input binary string
def input_plaintext():
    global PLAINTEXT, INPUT, OUTPUT
    PLAINTEXT = input("Input plaintext: ")
    INPUT = [c for c in string.ascii_uppercase[:len(PLAINTEXT)]]
    print(INPUT)
    output = input("Input output wire name: ")
    OUTPUT = output.split()

#save wire name
def save_wire(gate):
    global WIRE
    for w in gate[2:]:
        if(not w in WIRE):
            WIRE.append(w)
    return 0

#circuit description
def input_circuit():
    global CIRCUIT
    while True:
        input_gate = input("Input logic gate: ")
        if input_gate == "":
            break
        gate = input_gate.split()
        if len(gate) != 5:
            print("Format error!")
            continue
        if CIRCUIT.get(gate[0]) != None:
            print("Gate name exist!")
            continue
        save_wire(gate)
        key = gate.pop(0)
        CIRCUIT[key] = gate

#random letters and digits generation
def random_string():
    global GARBLED_WIRE, WIRE
    for c in WIRE:
        w = []
        w.append(''.join(random.choices(string.ascii_uppercase + string.digits, k=5)))
        w.append(''.join(random.choices(string.ascii_uppercase + string.digits, k=5)))
        GARBLED_WIRE[c] = w

#quickly return md5 hash value
def md5(data):
    m = hashlib.md5()
    m.update(data.encode('utf-8'))
    return m.hexdigest()

#garbled all truth table
def garbled_gate(gate):
    gatetable = []
    for x in [0, 1]:
        for y in [0, 1]:
            s = GARBLED_WIRE[gate[1]][x] + GARBLED_WIRE[gate[2]][y]
            if gate[0] == "AND":
                gatetable.append(md5(s + GARBLED_WIRE[gate[3]][int(x and y)]))
            elif gate[0]  == "NAND":
                gatetable.append(md5(s + GARBLED_WIRE[gate[3]][int(not(x and y))]))
            elif gate[0]  == "OR":
                gatetable.append(md5(s + GARBLED_WIRE[gate[3]][int(x or y)]))
            elif gate[0]  == "NOR":
                gatetable.append(md5(s + GARBLED_WIRE[gate[3]][int(not(x or y))]))
            elif gate[0] == "XOR":
                gatetable.append(md5(s + GARBLED_WIRE[gate[3]][int(x != y)]))
            elif gate[0] == "XNOR":
                gatetable.append(md5(s + GARBLED_WIRE[gate[3]][int(not(x != y))]))
            else:
                print(gate[0], "not found")
    random.shuffle(gatetable)
    return gatetable

#generate garble circuit with random string and garbled truth table
def generate_garbled_circuit():
    global GARBLED_TRUTH_TABLE
    random_string()
    for gate in CIRCUIT.items():
        table = garbled_gate(gate[1])
        GARBLED_TRUTH_TABLE[gate[0]] = table

#find hash value in the truth table
def find_table(md5hash, gate):
    for i in GARBLED_TRUTH_TABLE[gate]:
        if md5hash == i:
            return i, True
    return 0, False

#test the function of the garbled circuit
def decrypt_garbled_circuit():
    wire = dict()
    for key, i in enumerate(PLAINTEXT):
        wire[INPUT[key]] = GARBLED_WIRE[INPUT[key]][int(i)]
    for gate in CIRCUIT.items():
        for output in GARBLED_WIRE[gate[1][3]]:
            answer = []
            md5hash = md5(wire[gate[1][1]] + wire[gate[1][2]] + output)
            answer = find_table(md5hash, gate[0])
            if answer[1] == True:
                wire[gate[1][3]] = output
                break
    ans = dict()
    for w in OUTPUT:
        ans[w] = GARBLED_WIRE[w].index(wire[w])
    return ans

def main():
    print("-Garbled Circuit-")
    input_plaintext()
    input_circuit()
    generate_garbled_circuit()
    print("Garbled wire:")
    print(GARBLED_WIRE)
    print("Garbled truth table:")
    print(GARBLED_TRUTH_TABLE)
    print("Answer of decryption:", decrypt_garbled_circuit())

#main function execution
if __name__ == "__main__":
    main()