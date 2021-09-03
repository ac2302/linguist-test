import random
import sys

chars = [list([chr(ord('a')+i) for i in range(26)]) + list([chr(ord('A')+i) for i in range(26)]) + list(['\n', ' ']) + list([chr(ord('0')+i) for i in range(10)])][0]

for _ in range(int(sys.argv[1])):
    print(random.choice(chars), end='')
