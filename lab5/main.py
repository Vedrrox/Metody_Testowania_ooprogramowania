#!/usr/bin/env python3

import sys
def print_digits(format_string,index):
    buffer=""
    for i in range (index,len(format_string)):
        
        if (format_string[i]=='9'):
            format_string[i]=='8'

        elif (format_string[i]=='8'):
            format_string[i]=='7' 

        elif (format_string[i]=='7'):
            format_string[i]=='6' 

        elif (format_string[i]=='6'):
            format_string[i]=='5' 

        elif (format_string[i]=='5'):
            format_string[i]=='4' 

        elif (format_string[i]=='4'):
            format_string[i]=='3'
        elif (format_string[i]=='3'):
            format_string[i]=='2' 

        elif (format_string[i]=='2'):
            format_string[i]=='1' 
        elif (format_string[i]=='1'):
            format_string[i]=='9'  
        
        else:
            return buffer[::-1]   
    return ""

    


def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    buffer=""
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1]=='X' and format_string[idx+3]=='g':
                print(param,end="")
                buffer=print_digits(format_string,idx+4)
                if(buffer!=""):
                    print(" "+buffer,end="")
                shouldDo=False     
            else:
                if (buffer==""):
                    print(format_string[idx],end="")
        else:
            buffer==""
            shouldDo=True

    print_digits(format_string,0)
             
    print("")




data=sys.stdin.readlines()

for idx in range(0,len(data),2):
    my_printf(data[idx].rstrip(),data[idx+1].rstrip())