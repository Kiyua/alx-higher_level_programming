#!/usr/bin/python3
for i in range(ord('A'), ord('Z') + 1):
    print("{}".format(chr(i)), end="" if chr(i) != "Z" else "\n")
