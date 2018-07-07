from pynput import keyboard
from driver import Driver
import argparse

# current hot keys for testing
# need to make it configurable
COMBINATIONS = [
	{keyboard.Key.ctrl_l, keyboard.Key.shift, keyboard.KeyCode(char='p')},
	{keyboard.Key.ctrl_l, keyboard.Key.shift, keyboard.KeyCode(char='P')}, 
]

current = set()

browser = Driver()

def execute():
	global browser
	browser.pauseplay()

def on_press(key):
	if any([key in COMBO for COMBO in COMBINATIONS]):
		current.add(key)
		if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
			execute()
			exit()

def on_release(key):
	if any([key in COMBO for COMBO in COMBINATIONS]):
		current.remove(key)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Play and pause youtube videos with hotkeys.")
	parser.add_argument("-url", type=str, dest="url", help="url for youtube video/playlist")
	url = parser.parse_args().url
	browser.start(url)
	with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
		listener.join()
