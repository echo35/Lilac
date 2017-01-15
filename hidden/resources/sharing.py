from mod_python import util, apache
import os, urllib2

def getdata_file(req):
	name = urllib2.unquote(get_arg(req, "path"))
	set_mime(req, name.split(".")[-1], name)
	directory = to_path("$data/shared/")
	size = os.stat(directory + name).st_size
	offset1 = 0
	offset2 = size-1
	try:
		if "Range" in req.headers_in:
			section = str(req.headers_in["Range"]).replace("bytes=", "").split("-")
			offset1 = int(section[0])
			if len(section) == 2 and len(section[1]) > 0:
				offset2 = int(section[1])-1
			req.status = apache.HTTP_PARTIAL_CONTENT
			req.headers_out["Content-Range"] = "bytes %d-%d/%d" % (offset1, offset2, size)
	except:
		pass
	try:
		if os.path.exists(directory + name):
			with open(directory + name, "r") as f:
				req.set_content_length(offset2+1-offset1)
				req.write(f.read()[offset1:offset2])
				return apache.OK
	except:
		pass
	return "404"

def get_img(req):
	name = urllib2.unquote(get_arg(req, "name"))
	set_mime(req, "jpg", name)
	directory = "/var/www/babylon/data/shared/img/"
	if os.path.exists(directory + name):
		with open(directory + name, "r") as f:
			req.set_content_length(os.stat(directory + name).st_size)
			return f.read()
	return "404"
