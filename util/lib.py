from pynput import keyboard
import sys

COMMAND_ELEMENTS = {
	'pauseplay': 'ytp-play-button',
	'next': 'ytp-next-button'
}

COMBINATIONS = {
	'darwin': { # combinations for mac machines
		'next': [ # combinations for playing the next video
			{keyboard.Key.cmd, keyboard.Key.shift, keyboard.Key.shift_r}
		],
		'pauseplay' : [ # combinations for pausing/playing a video on mac machines
			{keyboard.Key.cmd, keyboard.Key.shift, keyboard.Key.alt_r}
		],
		'quit': [ # combinations for shutting everything down on mac machines
			{keyboard.Key.cmd, keyboard.Key.ctrl, keyboard.Key.alt}
		],
	}
}

def get_combinations():
	if sys.platform == 'darwin':
		return COMBINATIONS['darwin']

def get_command_elem(command):
	return COMMAND_ELEMENTS.get(command, None)