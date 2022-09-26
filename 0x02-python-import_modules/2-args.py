#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    length = len(args)
    print("{} argument{}{}".format(length - 1, "" if length == 2 else "s",
                                   ":" if length > 1 else "."))
    for i in range(1, length):
        print("{}: {}".format(i, args[i]))
