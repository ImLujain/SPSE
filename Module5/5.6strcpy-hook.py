#!/usr/bin/env python
import sys
sys.path.append('C:/Program Files (x86)/Immunity Inc/Immunity Debugger')
sys.path.append('C:/Program Files (x86)/Immunity Inc/Immunity Debugger/Libs')


import immlib
from immlib import LogBpHook

DESC = "Leverages BpHook to Show Function Elements in Table Form"

class MyBpHook(LogBpHook) :
    def __init__(self, fctName) :
        LogBpHook.__init__(self)
        self.fctName = fctName

    def run(self, regs):
        imm = immlib.Debugger()
        info = {}
        # Get EIP location
        info['ESP'] = (imm.readLong(regs['ESP']))
        espval = str(info ['ESP'])
        # Get address of first argument - destination to copy to
        info['Argument1'] = (imm.readLong(regs['ESP'] + 4))
        arg1val= str(info['Argument1'])
        # Get address of second argument - source to input into function
        info['Argument2'] = (imm.readLong(regs['ESP'] + 8))
        arg2val = str(info['Argument2'])
        # Get the value (string) of the second argument
        info['String'] = imm.readString(info['Argument2'])
        stringval = info['String']
        # Determine the length of the second argument value
        info['StringLength'] = len(str(info['String']))
        strlenval = info['StringLength']
        imm.log("ESP :" + espval + " arg1 : " + arg1val + " arg2 :" + arg2val + "String :" + stringval) 

        # Build and display a table showing keys/values for each element
        td = imm.createTable("Function %s Elements" %self.fctName, ['Element', 'Value'])
        for key in info:
            td.add(0, [str(key), str(info[key])]) 

def main(args) :
    imm = immlib.Debugger()

    # Specify function to hook here:
    fctName = "msvcrt.strcpy"

    # Get address of the function
    fctAddr = imm.getAddress(fctName)

    # Instantiate a new hook
    hook = MyBpHook(fctName)
    hook.add(fctName, fctAddr)

    imm.log("Function %s at 0x%08x has been hooked" % (fctName, fctAddr))
    
    message = "Function %s has been hooked." %fctName
    return message
