# SHA256 with Garbled Circuit
# python 3.6
# encoding=utf-8

import os
import queue
import string
import garbled_circuit

class sha256:
    _h = [] # data block of variables h[0] .. h[7]
    _k = [] # data block of constants k[0] .. k[63]
    message = []

    # initial
    def __init__(self, plaintext):
        self.text_to_bits(plaintext)
        print(os.path.abspath('.'))
        # load constant data block
        if os.path.isfile("sha256_h.txt") and os.path.isfile("sha256_k.txt"):
            self.read_h()
            self.read_k()
            self.pre_process()
            self.process()
        else:
            print("h.txt & k.txt not found")
            exit(0)
    
    # pre-processing
    def pre_process(self):
        self.message += '1'
        while len(self.message) % 448 != 0:
            self.message += '0'
        self.message += '{0:064b}'.format(len(self.message))
        print(len(self.message))

    # process the message in successive 512-bit chunks
    def process(self):
        chunks = [self.message[i:i + 512] for i in range(0, len(self.message), 512)]
        for chunk in chunks:
            w = self.extend(chunk)
            al = self._h
            self.main_loop(w, al)
            for i in range(0, 8):
                self._k[i] = format(int(self._k[i], 2) + int(al[i], 2), "032b")

    
    # extend the sixteen 32-bit words into sixty-four 32-bit words
    def extend(self, chunk):
        w = []
        for i in range(0, len(chunk), 32):
            w_ = chunk[i:i + 32]
            w.append(w_)
        for i in range(16, 64):
            s0 = self._sigma00(w[i - 15])
            s1 = self._sigma01(w[i - 2])
            w_ = format(int(w[i - 16], 2) + int(s0, 2) \
                 + int(w[i - 7], 2) + int(s1, 2), "032b")
            w.append(w_)
        return w

    # process main loop
    def main_loop(self, w, al):
        for i in range(0, 64):
            s0 = self._sigma10(al[0])
            ma = self._ma(al[0], al[1], al[2])
            t2 = format(int(s0, 2) + int(ma, 2), "032b")
            s1 = self._sigma11(al[4])
            ch = self._ch(al[4], al[5], al[6])
            t1 = format(int(al[7], 2) + int(s1, 2) + int(ch, 2) \
                 + int(self._k[i], 2) + int(w[i], 2), "032b")
            al[7] = al[6]
            al[6] = al[5]
            al[5] = al[4]
            al[4] = format(int(al[3], 2) + int(t1, 2), "032b")
            al[3] = al[2]
            al[2] = al[1]
            al[1] = al[0]
            al[0] = format(int(t1, 2) + int(t2, 2), "032b")

    # s0
    def _sigma00(self, x):
        pass

    # s1
    def _sigma01(self, x):
        pass

    # S0
    def _sigma10(self, x):
        pass

    # S1
    def _sigma11(self, x):
        pass

    # Ma
    def _ma(self, a, b, c):
        pass

    # Ch
    def _ch(self, a, b, c):
        pass

    # produce the final hash value
    # transform binary to heximal
    def hexdigest(self):
        bits = ''.join(l for l in self._h)
        return hex(int(bits, 2))

    # load variables from file
    def read_h(self):
        f = open("sha256_h.txt", "r")
        if f.mode == "r":
            lines = f.readlines()
            for line in lines:
                self._h.append(format(int(line, 16), "032b"))
        print(self._h)
        f.close()

    # load constants from file
    def read_k(self):
        f = open("sha256_k.txt", "r")
        if f.mode == "r":
            lines = f.readlines()
            for line in lines:
                line_ = line.split()
                for l in line_:
                    self._k.append(format(int(l, 16), "032b"))
        print(self._k)
        f.close()

    # load circuit
    def read_circuit(self):
        f = open("", "r")
        if f.mode == "r":
            # lines = f.readlines()
            # input_wire = lines.pop(0).split()
            # output_wire = lines.pop(0).split()
            # for line in lines:
            #     circuit.append(line)
            pass
        f.close()

    # transform text to binary
    def text_to_bits(self, text, encoding='utf-8', errors='surrogatepass'):
        bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
        self.message = bits.zfill(8 * ((len(bits) + 7) // 8))

def main():
    plaintext = input("")
    sha256_ = sha256(plaintext)
    print(sha256_.hexdigest)

# main function execution
if __name__ == "__main__":
    main()
