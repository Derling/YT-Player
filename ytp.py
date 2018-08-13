#!/usr/bin/env python
from pynput import keyboard
from driver import Driver
from util.lib import get_combinations, get_command_elem, get_logger
import argparse
import logging

logger = get_logger('ytp')

combinations = []

current = set()

browser = Driver()

last_command = None

def execute(command):
	global browser
	global last_command

	if command == 'quit':
		browser.quit()
	else:
		element = get_command_elem(command)
		browser.click_element(element)

	last_command = command

def key_in_combinations(key, combinations):
	return any([key in combo for combo in combinations])

def current_keys_match_combinations(current, combinations):
	return any(all(k in current for k in combo) for combo in combinations)

def on_press(key):
	for command in combinations:
		command_combos = combinations[command]
		if key_in_combinations(key, command_combos):
			current.add(key)
			if current_keys_match_combinations(current, command_combos):
				execute(command)

def on_release(key):
	if key in current:
		current.remove(key)
	if last_command == 'quit':
		return False

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="play and pause youtube videos with custom hotkeys.")
	parser.add_argument("url", type=str, help="url for youtube video/playlist")
	url = parser.parse_args().url
	combinations = get_combinations()
	browser.start(url)
	logger.info('browser opened')
	with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
		logger.info('listener starting')
		listener.join()
