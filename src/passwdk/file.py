import os, json

def load(conf):
	passwd_dir  = os.path.expanduser(os.path.expandvars(conf["PASSWD_DIR"]))
	passwd_file = passwd_dir + "/" + os.path.expandvars(conf["PASSWD_FILE"])
	if not os.path.isdir(passwd_dir):
		print "error: {0} is not a drectory".format(passwd_dir)
		exit(-1)

	if not os.path.exists(passwd_file):
		print "warning: {0} does not exists, creating it".format(passwd_file)
		save(conf, [])

	if not os.path.isfile(passwd_file):
		print "error: {0} is not file".format(passwd_file)
		exit(-1)

	f = open(passwd_file, "r")
	contents = json.load(f)
	f.close()
	return contents

def save(conf, data):
	passwd_dir  = os.path.expanduser(os.path.expandvars(conf["PASSWD_DIR"]))
	passwd_file = passwd_dir + "/" + os.path.expandvars(conf["PASSWD_FILE"])
	passwd_tmp  = passwd_file + ".passwdk.tmp"
	f = open(passwd_tmp, "w")
	json.dump(data, f, separators=(",", ": "), indent=2)
	f.flush()
	os.fsync(f.fileno())
	f.close()
	os.rename(passwd_tmp, passwd_file)
