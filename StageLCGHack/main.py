import os
import time
import json
from datetime import datetime


class LCGPseudoRandomGenerator:
    def __init__(self, a=48271, c=0, m=2**32, seed=None):
        self.a = a
        self.c = c
        self.m = m

        if seed is None:
            self.x0 = int(os.getpid() + time.time())
        else:
            self.x0 = seed

        self.x_prev = (self.a * self.x0 + self.c) % self.m

    def generate_number(self, num_range=None):
        self.x_prev = (self.a * self.x_prev + self.c) % self.m

        if num_range is None:
            return self.x_prev
        else:
            return int((self.x_prev / (self.m - 1)) * (num_range[1] - num_range[0]) + num_range[0])


lcg = LCGPseudoRandomGenerator()

lcg_output = {}

file_time_prefix = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")

for x in range(4700):
    key = str(x).zfill(2)

    number_generated = lcg.generate_number([15962948, 15967649])

    lcg_output[key] = number_generated

    print(f"{x} - {number_generated}")

with open(f"lcg_output_{file_time_prefix}.json", 'w') as output_file:
    json.dump(lcg_output, output_file, indent=4)


def get_dv(self, chave):

    peso_dv = [4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 9,
               8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    dv_calculado = 11 - (sum([int(char) * peso_dv[i]
                         for i, char in enumerate(chave[0:43])]) % 11)

    if dv_calculado == 10 or dv_calculado == 11:

        return '0'

    else:

        return str(dv_calculado)
