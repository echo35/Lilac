from mod_python import util, apache
import commands

def getsignal_exec(req):
	name = urllib2.unquote(get_arg(req, "path"))
	args = get_arg(req, "args")
	if args == None:
		args = ""
	args = urllib2.unquote(args)
	set_mime(req, name.split(".")[-1], name)
	directory = to_path("$data/scripts/")
	if os.path.exists(directory + name):
		try:
			if name[-3:] == ".py":
				with open(directory + name, "r") as f:
					exec(f.read())
					return script(req, args)
			elif name[-3:] == ".sh":
				return commands.getstatusoutput("bash " + directory + name + " \"" + escape(args) + "\"")[1]
		except:
			return traceback.format_exc()
	return "404"

def escape(args):
	return args.replace("\"", "\\\"")
