import sys, complete
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
	complete.complete_options(parser, sys.argv[2])
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

def get(conf):
	parser = ArgumentParser(usage="%(prog)s get search terms")
	parser.add_argument("search", nargs="+", help="search terms")
	parser.add_argument("-p", dest="password", action="store_true", help="only password without ending new-line")
	complete.complete_options(parser, sys.argv[2])
	complete.complete_names_and_tags(conf, sys.argv[2])
	args = parser.parse_args(sys.argv[2:])

	def search(it):
		name = it["name"] in args.search
		tags = reduce(lambda b, s: b and "tags" in it and it["tags"].count(s) > 0, args.search, True)
		return name or tags

	for i, r in enumerate(filter(search, load(conf))):
		if i > 0: print
		if args.password:
			sys.stdout.write(r["pass"])
		else:
			print "name:\t{0}".format(r["name"])
			print "pass:\t{0}".format(r["pass"])

			if "user" in r: print "user:\t{0}".format(r["user"])
			if "mail" in r: print "mail:\t{0}".format(r["mail"])

			for o in r["othr"] if "othr" in r else []:
				print "{0}:\t{1}".format(o, r["othr"][o])

def main():
	valid_actions  = ["add", "get"]
	actions_parser = ArgumentParser()
	actions_parser.add_argument("action", choices=valid_actions, help="action to take")
	actions = actions_parser.parse_args(sys.argv[1:2])

	globals()[actions.action](config())
