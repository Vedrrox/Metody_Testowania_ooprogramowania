#!/usr/bin/env python3

import sys

def subtract(string1):
    string1 = int(string1)
    

    return str((string1*9+1)%10)


def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    paramInUse=False
    counter = 0
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'j':
                print(param,end="")
                shouldDo=False
                paramInUse=True
            elif paramInUse:
                if(format_string[idx].isdigit()):
                    if(format_string[idx]=='0'):
                        print(0,end="")
                    else:
                        print(subtract(format_string[idx],'1'),end="")
            else:
                print(format_string[idx],end="") 

           

    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())