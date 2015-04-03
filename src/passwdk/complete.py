import re
from file import load

def complete_options(parser, cmd):
	if cmd != "complete-options":
		return

	lines = filter(lambda l: re.match("[ ]+-[^h].*", l) ,parser.format_help().split('\n'))
	lines = map(lambda l: re.sub("[ ]+", " ", l), lines)
	lines = map(lambda l: re.sub("^ ", "", l), lines)
	lines = map(lambda l: re.sub(" ", ":", l, count=1), lines)
	lines.append("-h:show help message")

	for l in lines: print l
	exit(0)

def complete_names_and_tags(conf, cmd):
	if cmd != "complete-names-and-tags":
		return

	data  = load(conf)
	lines = set()
	for d in data:
		lines.add(d["name"])
		lines.update(d["tags"] if "tags" in d else [])

	for l in lines: print l
	exit(0)
