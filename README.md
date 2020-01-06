# **Garbled Circuit**

> Garbled Circuit with two version. Version 1 is unfinished but only has a basic concept with garbled circuit.
> Version 2 has been finished the most important encryption function.

## Version 1
> Realize the manual input custom gate circuit, and then synthesize any custom combination circuit, and get the truth table function, but there is a requirement that each layer of the combination circuit need to have at least one gate.

## Version 2 (Main)
### Basic Function
> Implement that all circuits have to read from "circuit" directory. By the way, only support the combinational circuit and must be with hierarchy. All of the basic functions have defined in the "class" definition, so the user could use it easier.

#### Circuit Description Format
The first line contains all of the circuit input name tag, separate with space.  
The second line contains all of the circuit output name tag, separate with space.  
The next ***n*** lines are the two-input logic gates description, each line contains the logic type, first input name, second input name, and output name.

#### Input Format
The input only have one line string ***s*** with 0 or 1.  
It would read the circuit description file from `./circuit/gc`

#### Output Format
Output ***lo*** lines, which indicates the number of circuit output wire and each line has a name tag and a number either 0 or 1.

#### Technical Specification
The input string length ***l<sub>s</sub>*** must same as the number of circuit input wire.

#### Sameple Circuit Description
```
i1 i2 i3 i4
o1 o2 o3 o4 o5
XOR i1 i2 o1
AND i2 i3 o2
OR i3 i4 o3
NAND o1 i1 o4
NOR o2 o3 o5
```

#### Sample Input:
```
1010
```

#### Sample Output:
```
o1 1
o2 0
o3 1
o4 0
o5 0
```

### SHA256 with Garbled Circuit
> As same as the basic function, I also wrote it in the "class", and easily call the `garbled_circuit` function to calculate.

#### Usage
> Using `python sha256_gc.py` to generate the input randomly or `python sha256_gc.py <arg1>` to indicate the string to hash.

#### Example

## Contribution
[click me](https://hackmd.io/@edDnIx-xTO2Y79IC9tqYgg/B1wep6z9r)
