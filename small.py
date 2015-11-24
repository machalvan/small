#!/usr/bin/env python
import sys

class mc:
	inc = "+"
	display = "."
	read = ","

class ma():
	board = 0
	def inc():
		ma.board = ma.board+1

	def display():
		print(chr(ma.board),end="")

	def read():
		ma.board = ord(input("input:")[0])

bsFile = open(sys.argv[1], "r")
bsFile = ''.join(list(bsFile))

loop = True

i = 0

pos = bsFile[i]

while loop:
	pos = bsFile[i]
	if(pos == mc.inc):
		ma.inc()
	if(pos == mc.display):
		ma.display()
	if(pos == mc.read):
		ma.read()
	
	if(ma.board > 250):
		ma.board = 0
	i = i + 1
	if i == len(bsFile):
		loop = False
		print("\n")
