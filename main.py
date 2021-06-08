#!/usr/bin/env python

#Source of Morse is https://morsecode.scphillips.com/morse2.html


import RPi.GPIO as GPIO
import time
import os

# 'step'	= 1    					/signal on/off
# 'dit'		= step					/dot
# 'dash'	= 3 * step				/dash
# 'pause'	= 3 * step 				/pause after letters
# 'space'	= 7 * step				/pause between words
# 
#
# Average number of letters for English word is 4.79
# However, the most common range is [5,6]

non   = 'non'
space = ' '
pause = 0.2 #assign from user input
tWork = 0.5 #assing from user input 

Led   = 11

morse = [
	[space],			# ' ' /32
	['-.-.--'],			# !
	['.-..-.'],			# "
	[none],				# #
	[none],				# $
	[none],				# %	
	['.-...'],			# & V
	['.----.'],			# ' V
	['-.--.'],			# (
	['-.--.-'],			# )
	[none],				# *
	['.-.-.'],			# +
	['--..--'],			# ,
	['-....-'],			# -
	['.-.-.-'],			# .
	['-..-.'],			# /
	['----'],			# 0 V
	['.---'],			# 1 V
	['..---'],			# 2 V
	['...--'],			# 3 V
	['....-'],			# 4 V
	['.....'],			# 5 V
	['-....'],			# 6 V
	['--...'],			# 7 V
	['---..'],			# 8 V
	['----.'],			# 9 V
	['---...'],			# :
	[none],				# ;
	[none],				# <
	[none],				# >
	['..--..'],			# ?
	['.--.-.'],			# @ V
    ['.-'],    			# A /65
    ['-...'],    		# B
    ['-.-.'],    		# C
    ['-..'],			# D
    ['.'],  			# E
    ['..-.'],    		# F
    ['--.'],    		# G
    ['....'],    		# H
    ['..'],    			# I
    ['.---'],   		# J
    ['-.-'],    		# K
    ['.-..'],    		# L
    ['--'],    			# M
    ['-.'],    			# N
    ['---'],    		# O
    ['.--.'],    		# P
    ['--.-'],   		# Q
    ['.-.'],    		# R
    ['...'],    		# S
    ['-'],    			# T
    ['..-'],    		# U
    ['...-'],   		# V
    ['.--'],    		# W
    ['-..-'],   		# X
    ['-.--'],   		# Y
    ['--..']     		# Z
]


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Led, GPIO.OUT)
    GPIO.output(Led, GPIO.HIGH)



def destroy():
    GPIO.output(Led, GPIO.HIGH)
    GPIO.cleanup()

def outPut(raer):
    for jo in range(4):
        if (morse[raer][jo] == '.'):
            print '...led on'
            GPIO.output(Led, GPIO.LOW)
            time.sleep(tWork)
            os.system('clear')
            print 'led off...'
            GPIO.output(Led, GPIO.HIGH)
            time.sleep(pause)
            os.system('clear')
        elif (morse[raer][jo] == '-'):
            print '...led on'
            GPIO.output(Led, GPIO.LOW)
            time.sleep(3 * tWork)
            print 'led off...'
            GPIO.output(Led, GPIO.HIGH)
            time.sleep(pause)
        else:
            break
    #letter is done, pause for 0.5 seconds
    time.sleep(1)


def exe():
    while True:
        os.system('clear')
        print 'Enter the string w/o spaces'
        inp = raw_input()
        inp = inp.upper()
        for i in range(len(inp)):
            num = ord(inp[i]) - 65
            if num >= 0 and num <= 25:
                outPut(num)
        
        

if __name__ == '__main__':
    setup()
    try:
        exe()
    except KeyboardInterrupt:
        destroy()



