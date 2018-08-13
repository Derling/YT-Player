from pynput import keyboard
import logging
import sys

FORMATTER = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

COMMAND_ELEMENTS = {
	'pauseplay': 'ytp-play-button',
	'next': 'ytp-next-button'
}

COMBINATIONS = {
	'darwin': { # combinations for mac machines
		'next': [
			{keyboard.Key.cmd, keyboard.Key.shift, keyboard.Key.cmd_r}
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

def get_logger(name, level=logging.INFO):
	# Creates a logger
	handler = logging.StreamHandler()
	handler.setFormatter(FORMATTER)

	logger = logging.getLogger(name)
	logger.setLevel(level)
	logger.addHandler(handler)

	return logger

def get_combinations():
	# Returns combinations based on operating system
	if sys.platform == 'darwin':
		return COMBINATIONS['darwin']
	elif sys.platform == 'win32':
		return COMBINATIONS['win32']
	else:
		pass

def get_command_elem(command):
	# Returns the corresponsing element class name for the given command
	return COMMAND_ELEMENTS.get(command, None)