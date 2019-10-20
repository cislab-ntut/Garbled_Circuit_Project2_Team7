#Garbled Circuit
#python3.6
#coding=utf-8

import random
import hashlib
import string

PLAINTEXT = ""

INPUT = []
#GARBLED_INPUT = dict()
WIRE = []
GARBLED_WIRE = dict()
CIRCUIT = dict()
#TRUTH_TABLE = dict()
GARBLED_TRUTH_TABLE = dict()

#def initial():

#input binary string
def input_plaintext():
    global PLAINTEXT, INPUT
    PLAINTEXT = input("Input plaintext: ")
    INPUT = [c for c in string.ascii_uppercase[:len(PLAINTEXT)]]
    print(INPUT)

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
        GARBLED_WIRE[c] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

def md5(data):
    m = hashlib.md5()
    m.update(data.encode('utf-8'))
    return m.hexdigest()

def garbled_gate(gate):
    gatetable = []
    for x in [0, 1]:
        for y in [0, 1]:
            md5hash = md5(''.join(GARBLED_WIRE[gate[1]] + str(x) + GARBLED_WIRE[gate[2]] + str(y)))
            if gate[0] == "AND":
                gatetable.append([md5hash ,GARBLED_WIRE[gate[3]] + str(x and y)])
            elif gate[0]  == "NAND":
                gatetable.append([md5hash ,GARBLED_WIRE[gate[3]] + str(int(not(x and y)))])
            elif gate[0]  == "OR":
                gatetable.append([md5hash ,GARBLED_WIRE[gate[3]] + str(x or y)])
            elif gate[0]  == "NOR":
                gatetable.append([md5hash ,GARBLED_WIRE[gate[3]] + str(int(not(x or y)))])
            else:
                print(gate[0], "not found")
    random.shuffle(gatetable)
    return gatetable

def generate_garbled_circuit():
    global GARBLED_TRUTH_TABLE
    random_string()
    for gate in CIRCUIT.items():
        table = garbled_gate(gate[1])
        GARBLED_TRUTH_TABLE[gate[0]] = table

#def decryption():

def main():
    print("-Garbled Circuit-")
    #initial()
    input_plaintext()
    input_circuit()
    generate_garbled_circuit()
    print(GARBLED_WIRE)
    print(GARBLED_TRUTH_TABLE)

#main function execution
if __name__ == "__main__":
    main()