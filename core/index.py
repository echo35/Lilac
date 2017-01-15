#!/usr/bin/env python2
import os, traceback, time, urllib2

project_name = ")_-_PROJECT_NAME_-_("

def to_path(string):
	return string.replace("$", "/var/www/%s/" % (project_name))

for dependency in "zero.py sharing.py pages.py execute.py".split(" "):
	execfile(to_path("$hidden/resources/") + dependency)

page_404 = '''
<html>
	<body>
		<center>
			<br>
			<font style="font-size: 56pt">404: Page Not Found</font>
		</center>
	</body>
</html>
'''[1:-1]

def search_archive(req):
	link_id = get_arg(req, "p")
	index_file = ""
	extension = "html"
	with open(to_path("$data/index.txt"), "r") as f:
		for line in f.read().split('\n'):
			if line.split(' ')[0] == link_id:
				extension = line.split()[1]
				index_file = ' '.join(line.split()[2:])
	index_file = to_path(index_file)
	set_mime(req, extension, index_file)
	if len(index_file) > 0:
		if extension == "link":
			return "<html><script type='text/javascript'>window.location = '{0}';</script></html>".format(index_file)
		elif os.path.exists(index_file):
			size = os.stat(index_file).st_size
			req.set_content_length(size)
			with open(index_file, "r") as f:
				return f.read()
	return "404"

def index(req):
	try:
		link_id = get_arg(req, 'p')
		if link_id == None:
			# return under_construction(req)
			return getpage_web(req)
		else:
			try:
				if get_arg(req, "silent") != "please":
					log("$logs/site_access.log", "[{0}] {1} accessed {2}. Browser: {3}".format(time.strftime('%y-%m-%d %H:%M:%S'), '%15s' % getdata_ip(req), link_id, get_useragent(req)))
			except:
				log("$logs/site_access.log", "[{0}] {1} accessed {2}. Browser: {3}".format(time.strftime('%y-%m-%d %H:%M:%S'), '%15s' % getdata_ip(req), link_id, get_useragent(req)))
		html = "404"
		if link_id == "ipaddr":
			return getdata_ip(req)
		elif link_id == "file":
			html = getdata_file(req)
		elif link_id == "web":
			html = getpage_web(req)
		elif link_id == "color":
			html = getpage_color(req)
		elif link_id == "sha256":
			html = gethash_file(req)
		elif link_id == "exec":
			html = getsignal_exec(req)
		if html != "404":
			return html
		else:
			html = search_archive(req)
			if html != "404":
				return html
	except:
		if getdata_ip(req)[:8] == "192.168.":
			return traceback.format_exc()
		pass
	return page_404
