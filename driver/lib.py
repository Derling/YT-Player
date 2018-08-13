AUDIO_CONTROL = 'ytp-play-button'

ELEMENT_MESSAGES = {
	'ytp-next-button': "playing next song",
	'ytp-play-button': {
		True: "pausing song",
		False: "unpausing song"
	},
}

def get_element_msg(element_class, status):
	# Returns a message base on the element and player status
	msgs = ELEMENT_MESSAGES[element_class]
	if type(msgs) == dict:
		return msgs[status]
	return msgs