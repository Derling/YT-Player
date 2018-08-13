AUDIO_CONTROL = 'ytp-play-button'

ELEMENT_MESSAGES = {
	'ytp-next-button': "playing next song",
	'ytp-play-button': {
		True: "pausing song",
		False: "unpausing song"
	},
}

def get_element_msg(command, status):
	msgs = ELEMENT_MESSAGES[command]
	if type(msgs) == dict:
		return msgs[status]
	return msgs