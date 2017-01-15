#!/usr/bin/env python2

def getpage_color(req):
	html = """<!DOCTYPE html><html><body style="background-color:#%s"></body></html>""" % (get_arg(req, "hex"))
	return html

def getpage_web(req):
	with open(to_path("$data/html/web.html"), "r") as f:
		html = f.read()
	return html

def gethash_file(req):
	from hashlib import sha256
	try:
		tmp_file = req.form["file"].file
		return sha256(tmp_file.read()).hexdigest()
	except:
		return "no file"
