#Source of Morse is https://morsecode.scphillips.com/morse2.html

import RPi.GPIO as GPIO
from time import sleep
from os import name as os_name
from os import system

"""
	'step'	= 1    				/signal on/off
	'dit'	= step				/dot
	'dash'	= 3 * step			/dash
	'pause'	= 3 * step 			/pause after letters
	'space'	= 7 * step			/pause between words
"""

# Base time for one symbol
BASE_TIME = 0.5
# Pin Number where LED is located
# Refer to
LED_PIN   = 11

# Dictionary with all acceptable characters
# New ones can be appended
MORSE_CODE = {
	' ':  ' ',
	'!':  '-.-.--',
	'"':  '.-..-.',
	'&':  '.-...',
	'\'': '.----.',
	'(':  '-.--.',
	')':  '-.--.-',
	'+':  '.-.-.',
	',':  '--..--',
	'-':  '-....-',
	'.':  '.-.-.-',
	'/':  '-..-.',
	'0':  '----',
	'1':  '.---',
	'2':  '..---',
	'3':  '...--',
	'4':  '....-',
	'5':  '.....',
	'6':  '-....',
	'7':  '--...',
	'8':  '---..',
	'9':  '----.',
	':':  '---...',
	'?':  '..--..',
	'@':  '.--.-.',
    'A':  '.-',
    'B':  '-...',
    'C':  '-.-.',
    'D':  '-..',
    'E':  '.',
    'F':  '..-.',
    'G':  '--.',
    'H':  '....',
    'I':  '..',
    'J':  '.---',
    'K':  '-.-',
    'L':  '.-..',
    'M':  '--',
    'N':  '-.',
    'O':  '---',
    'P':  '.--.',
    'Q':  '--.-',
    'R':  '.-.',
    'S':  '...',
    'T':  '-',
    'U':  '..-',
    'V':  '...-',
    'W':  '.--',
    'X':  '-..-',
    'Y':  '-.--',
    'Z':  '--..']
}


def setup():
	"""
		Default preparation for pins on Raspberry Pi
		 - Setting up the 'LED_PIN'
	"""
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN,  GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.HIGH)


def destroy():
	"""
		Default cleanup for pins on Raspberry Pi
		 - Removing any binds from 'LED_PIN'
	"""
    GPIO.output(LED_PIN, GPIO.HIGH)
    GPIO.cleanup()


def clear():
	"""
		Screen(Terminal/Command Line) cleanup based
		on Operating System
	"""
	if os_name == 'nt':
		system('cls')
	else:
		system('clear')


def get_time_based_on_symbol(character: str):
	"""
		Returns the time when 'LED_PIN' should be on
	"""
	if (character == '.'):
		return BASE_TIME

	if (character == '-'):
		return 3 * BASE_TIME

	if (character == ' '):
		return 7 * BASE_TIME

	return 0


def light_diode(on_time: float):
	"""
		Lights the diode at 'LED_PIN' for 'on_time' secs.
	"""
	GPIO.output(LED_PIN, GPIO.LOW)
	sleep(on_time)
	GPIO.output(LED_PIN, GPIO.HIGH)


def display_process(string: str, character: str):
	"""
		Outputs the message for user
	"""
	clear()
	print('Your phrase:')
	print(string)
	print('Letter being output:')
	print(character)


def output_letter(morse_code: str):
	"""
		If 'morse_code' output the symbols for given letter,
		then wait 'BASE_TIME'(wait between letters)
	"""
	for character in morse_code:
		on_time = get_time_based_on_symbol(character)
		light_diode(on_time)
		sleep(BASE_TIME)


def main():
    while True:
        clear()
        print('Enter the phrase:')
        string = input()
        for character in string.upper():
			display_process(string, character)
            output_letter( MORSE_CODE.get(character, "") )



if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()
