#!/usr/bin/env python

#5.6 PyHook skeleton


# to view all modules we press view> Executablemodules

import sys
sys.path.append('C:/Program Files (x86)/Immunity Inc/Immunity Debugger')
sys.path.append('C:/Program Files (x86)/Immunity Inc/Immunity Debugger/Libs')

import immlib
from immlib import AllExceptHook


class DemoHook (AllExceptHook) :

	def __init__(self):
		AllExceptHook.__init__(self)

	def run(self, regs):
		imm = immlib.Debugger()
		eip = regs['EIP']
		esp = regs['ESP']

		imm.log("EIP : 0x%08X ESP: 0x%08X"%(eip,esp))

		buf = imm.readString(esp)
		if len(buf):
                        imm.log('String len at ESP: %d\n %s' %(len(buf), buf))


def main(args):
	imm = immlib.Debugger()

	newHook = DemoHook()

	newHook.add("Demo Hook :)")

	return "SPSE Hooking PyCommand"	
