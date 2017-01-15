from mod_python import util, apache

def get_arg(req, arg):
        form = util.FieldStorage(req, keep_blank_values=1)
        return form.getfirst(arg)

def getdata_ip(req):
	return req.get_remote_host(apache.REMOTE_NOLOOKUP)

def get_useragent(req):
	req.add_common_vars()
	return req.subprocess_env.get('HTTP_USER_AGENT')

def under_construction(req):
	with open(to_path("$data/html/under_construction.html"), "r") as f:
		return f.read()

def set_mime(req, ext, index_file):
	req.headers_out['Content-Disposition'] = 'inline; filename="%s"' % index_file.split('/')[-1]
	if ext.lower() == 'jpg':
		req.content_type = 'image/jpeg'
	elif ext.lower() in ['png', 'gif', 'bmp']:
		req.content_type = 'image/' + ext.lower()
	elif ext.lower() == 'mp3':
		req.content_type = 'audio/mpeg'
	elif ext.lower() == 'mp4':
		req.content_type = 'video/mp4'
	elif ext.lower() == 'wav':
		req.content_type = 'audio/wav'
	elif ext.lower() == 'pdf':
		req.content_type = 'application/pdf'
	elif ext.lower() == 'html' or ext.lower() == 'link':
		req.content_type = 'text/html'
	elif ext.lower() == 'js':
		req.content_type = 'text/javascript'
	elif ext.lower() == 'download':
		req.content_type = "application/octet-stream"
		req.headers_out['Content-Disposition'] = 'attachment; filename="%s"' % index_file.split('/')[-1]
	else:
		req.content_type = 'text/plain'

def log(file, string):
	file = to_path(file)
	max_length = 800
	contents = []
	if os.path.exists(file):
		with open(file, 'r') as f:
			contents = f.read().split('\n')
	contents.append(string)
	if len(contents) > max_length:
		contents = contents[len(contents)-max_length:]
	for line in contents:
		if line == '\n':
			del(contents, line)
	with open(file, 'w') as f:
		f.write('\n'.join(contents))
	return 'OK'
