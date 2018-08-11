from pynput import keyboard
import sys

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