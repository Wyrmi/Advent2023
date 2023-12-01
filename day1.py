import fileinput
from pathlib import Path
import os
import sys
filepath = 'Advent2023/test.txt'
for line in fileinput.input(filepath, inplace = False):
       numbers = []
       for char in line:
              if char.isdigit():
                     numbers.append(int(char))
       for x in numbers:
              sys.stdout.write(str(x))
              sys.stdout.write(" ")
       sys.stdout.write('\n')
