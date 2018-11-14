import sys

from mysys import clear
clear()
print(sys.argv, len(sys.argv))

def print_sys_vars():
    for i in [sys.version, sys.copyright, sys.platform]:
        print("---> ", i)

print_sys_vars()
sa = sys.argv
if len(sa) < 2 :
    sys.exit()

with open(sa[1], "r", encoding = "utf8") as file:
    for line in file:
        print(line)

