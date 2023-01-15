#!/usr/bin/env python3

import sys

def my_printf(format_string, param):
    shouldDo=True
    if len(format_string) > 0:
        if shouldDo:
            positionZ = format_string.find("#.Z")
            if positionZ != -1:
                positionOfNumber = positionZ + 3
                NumberString = ""
                StringNumber = ""
                for i in range(positionOfNumber, len(format_string)):
                    if format_string[i].isnumeric():
                        NumberString += format_string[i]
                    else:
                        break
                StringNumberInt = int(NumberString)
                NumberInHex = hex(param)
                NumberInHex= NumberInHex[2:].rjust(StringNumberInt,'0')
                NumberInHex= NumberInHex.replace("a", "g")
                NumberInHex= NumberInHex.replace("b", "h")
                NumberInHex= NumberInHex.replace("c", "i")
                NumberInHex= NumberInHex.replace("d", "j")
                NumberInHex= NumberInHex.replace("e", "k")
                NumberInHex= NumberInHex.replace("f", "l")
                NumberInHex= NumberInHex.replace("0", "o")
                print(NumberInHex)
                shouldDo=False
            else:
                print(format_string)
        else:
            shouldDo=True
    else:
        print("String is empty")

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), int(data[i+1].rstrip()))
