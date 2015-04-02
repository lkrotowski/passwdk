import os

def post_add(conf, name):
	if "POST_ADD_HOOK" in conf:
		if "NEW_PASSWORD_NAME" in os.environ:
			del os.environ["NEW_PASSWORD_NAME"]

		passwd_dir = os.path.expanduser(os.path.expandvars(conf["PASSWD_DIR"]))
		hook_exec  = os.path.expandvars(conf["POST_ADD_HOOK"])

		os.chdir(passwd_dir)
		os.putenv("NEW_PASSWORD_NAME", name)
		os.putenv("PASSWD_FILE", os.path.expandvars(conf["PASSWD_FILE"]))
		os.system(hook_exec)
