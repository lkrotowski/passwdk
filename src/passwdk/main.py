import sys
from argparse import ArgumentParser
from config   import config
from file     import load, save
from hooks    import post_add

def add(conf):
	parser = ArgumentParser(usage="%(prog)s add arguments")
	parser.add_argument("-n", required=True, dest="name", help="password name")
	parser.add_argument("-u", dest="user", help="user name")
	parser.add_argument("-e", dest="email", help="email")
	parser.add_argument("-o", nargs=2, action="append", dest="other", metavar=("NAME", "VALUE"), help="other informations")
	parser.add_argument("-t", nargs="+", dest="tags", help="password tags")
	args = parser.parse_args(sys.argv[2:])

	if args.other != None:
		other = dict()
		for o in args.other:
			other[o[0]] = o[1]

	data = load(conf)
	pssw = raw_input("enter password: ")

	nrec = dict()
	nrec["name"] = args.name
	nrec["pass"] = pssw
	if args.user != None:
		nrec["user"] = args.user
	if args.email != None:
		nrec["mail"] = args.email
	if args.other != None:
		nrec["othr"] = other
	if args.tags != None:
		nrec["tags"] = args.tags

	data.append(nrec)
	save(conf, data)
	post_add(conf, nrec["name"])

def main():
	valid_actions  = ["add"]
	actions_parser = ArgumentParser()
	actions_parser.add_argument("action", choices=valid_actions, help="action to take")
	actions = actions_parser.parse_args(sys.argv[1:2])

	if actions.action == "add":
		add(config())
