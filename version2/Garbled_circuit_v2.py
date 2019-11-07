# Garbled Circuit
# python 3.6
# coding=utf-8

import random
import hashlib
import string

PLAINTEXT = ""

INPUT = []  # name of input line
OUTPUT = []  # name of output line
WIRE = dict()  # name of line
GARBLED_WIRE = dict()  # garbled name of line
CIRCUIT = [] # circuit description like verilog
GARBLED_TRUTH_TABLE = []  # garbled truth table

# generate random string
def keygen():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

# input binary string
def input_plaintext():
    global PLAINTEXT, INPUT, OUTPUT
    while True:
        PLAINTEXT = input("Input plaintext: ")
        input_wire = input("Input wire: ")
        INPUT = input_wire.split()
        if len(PLAINTEXT) == len(INPUT):
            break
    for c in INPUT:
        WIRE[c] = keygen()

    output_wire = input("Output wire: ")
    OUTPUT = output_wire.split()
    for c in OUTPUT:
        WIRE[c] = keygen()

    print(WIRE)

# save wire name
def save_wire(gate):
    global WIRE
    for w in gate[1:]:
        if (not w in WIRE.keys()):
            WIRE[w] = keygen()
    return 0

# circuit description
def input_circuit():
    global CIRCUIT
    while True:
        input_gate = input("Input logic gate: ")
        if input_gate == "":
            break
        gate = input_gate.split()
        if len(gate) != 4:
            print("Format error!")
            continue
        save_wire(gate)
        circuit = [WIRE[w] for w in gate[1:]]
        circuit.insert(0, gate[0])
        CIRCUIT.append(circuit)

# random letters and digits generation
def garbled_wire():
    global GARBLED_WIRE, WIRE
    for c in WIRE.values():
        w = []
        w.append(keygen())
        w.append(keygen())
        GARBLED_WIRE[c] = w

# generate md5 hash value
def get_md5hash(data):
    m = hashlib.md5()
    m.update(data.encode('utf-8'))
    return m.hexdigest()

# garbled all truth table
def garbled_gate(gate):
    gatetable = []
    for x in [0, 1]:
        for y in [0, 1]:
            s = GARBLED_WIRE[gate[1]][x] + GARBLED_WIRE[gate[2]][y]
            if gate[0] == "AND":
                gatetable.append(get_md5hash(s + GARBLED_WIRE[gate[3]][int(x and y)]))
            elif gate[0]  == "NAND":
                gatetable.append(get_md5hash(s + GARBLED_WIRE[gate[3]][int(not(x and y))]))
            elif gate[0]  == "OR":
                gatetable.append(get_md5hash(s + GARBLED_WIRE[gate[3]][int(x or y)]))
            elif gate[0]  == "NOR":
                gatetable.append(get_md5hash(s + GARBLED_WIRE[gate[3]][int(not(x or y))]))
            elif gate[0] == "XOR":
                gatetable.append(get_md5hash(s + GARBLED_WIRE[gate[3]][int(x != y)]))
            elif gate[0] == "XNOR":
                gatetable.append(get_md5hash(s + GARBLED_WIRE[gate[3]][int(not(x != y))]))
            else:
                print(gate[0], "not found")
    random.shuffle(gatetable)
    return gatetable

# generate garble circuit with random string and garbled truth table
def generate_garbled_circuit():
    global GARBLED_TRUTH_TABLE
    garbled_wire()
    for gate in CIRCUIT:
        table = garbled_gate(gate)
        GARBLED_TRUTH_TABLE.append(table)

# find hash value in the truth table
def find_table(md5hash, i):
    for key in GARBLED_TRUTH_TABLE[i]:
        if md5hash == key:
            return i, True
    return 0, False

# test the function of the garbled circuit
def decrypt_garbled_circuit():
    wire = dict()
    for key, i in enumerate(PLAINTEXT):
        wire[WIRE[INPUT[key]]] = GARBLED_WIRE[WIRE[INPUT[key]]][int(i)]
    for i, gate in enumerate(CIRCUIT):
        for s in GARBLED_WIRE[gate[3]]:
            answer = []
            md5hash = get_md5hash(wire[gate[1]] + wire[gate[2]] + s)
            answer = find_table(md5hash, i)
            if answer[1] == True:
                wire[gate[3]] = s
                break
    ans = dict()
    for w in OUTPUT:
        ans[w] = GARBLED_WIRE[WIRE[w]].index(wire[WIRE[w]])
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
    output = decrypt_garbled_circuit()
    print("Answer of decryption:")
    for key, i in output.items():
        print(key, i)

#main function execution
if __name__ == "__main__":
    main()
