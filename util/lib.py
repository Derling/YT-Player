from pynput import keyboard
import sys

COMMAND_ELEMENTS = {
	'pauseplay': 'ytp-play-button',
	'next': 'ytp-next-button'
}

COMBINATIONS = {
	'darwin': { # combinations for mac machines
		'next': [
			{keyboard.Key.cmd, keyboard.Key.shift, keyboard.Key.shift_r}
		],
		'pauseplay' : [
			{keyboard.Key.cmd, keyboard.Key.shift, keyboard.Key.alt_r}
		],
		'quit': [
			{keyboard.Key.cmd, keyboard.Key.ctrl, keyboard.Key.alt}
		],
	},
	'win32': { # combinations for windows machines
		'next': [
			{keyboard.Key.ctrl_l, keyboard.Key.shift, keyboard.KeyCode.from_char(char='.')}
		],
		'pauseplay': [
			{keyboard.Key.ctrl_l, keyboard.Key.shift, keyboard.KeyCode.from_char(char=',')}
		],
		'quit': [
			{keyboard.Key.ctrl_l, keyboard.Key.shift, keyboard.Key.alt_l}
		]
	}
}

def get_combinations():
	if sys.platform == 'darwin':
		return COMBINATIONS['darwin']
	elif sys.platform == 'win32':
		return COMBINATIONS['win32']
	else:
		pass

def get_command_elem(command):
	return COMMAND_ELEMENTS.get(command, None)