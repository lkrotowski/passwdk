from collections import namedtuple
from os          import getenv
from shlex       import shlex
from sys         import exit

def config():
	config_file = getenv("HOME") + "/.passwdkrc"
	config_data = {}
	try:
		lexer = shlex(open(config_file), posix=True)
		def zero_state(initial=False):
			state = namedtuple("state", ["line", "befeq", "envvr", "name", "value"])
			state.line  = -1 if initial else lexer.lineno
			state.befeq = True
			state.name  = ""
			state.value = ""
			return state

		state = zero_state(True)
		while (True):
			token = lexer.get_token()
			if token == None:
				break
			if state.line == -1:
				state.line = lexer.lineno

			if state.befeq:
				if token != "=":
					state.name += token
				else:
					state.befeq = False
			else:
				state.value += token

			if state.line != lexer.lineno:
				if state.value != "":
					config_data[state.name] = state.value
					state = zero_state()
				else:
					state.line = lexer.lineno
	except IOError as e:
		print "error: config file {0} could not be read, reason: {1}".format(config_file, e.strerror)
		exit(-1)
	return config_data
