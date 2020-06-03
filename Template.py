"""
CTEC 121
<your name>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
from math import *
def main():
    '''
    x = 1
    y = 2
    z = 3
    print("x: {0}, y:{1}, z:{2}".format(x,y,z))

    print('pi:',pi,"e:",e)
    print("pi: {0:10.2f}, e: {1:10.4f}".format(pi,e))
    '''

    #file processing, no sample text but copying demo
    '''
    infile = open("filename", 'r')
    print(infile)

    wholefiletext= infile.read()
    print(wholefiletext)

    wholefiltext = infile.read()
    print("*",wholefiletext, "*',sep="")
    
    infile.seek(5)
    wholefiltext = infile.read()
    print("*",wholefiletext, "*',sep="")
    '''

    #dictionaries

    dict1 ={}
    print(dict1)
    dict2 = {}
    dict2[1]="one"
    dict2[2]="two"
    dict2[3]="three"
    print(dict2) 

    dict1 = {1: 'one', 2: 'two', 3: 'three'}
    print(dict1)

    print(dict1[2])

    print(dict1.keys())
    print(dict1.values())
    print(dict1.items())


main()    