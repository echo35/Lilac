def script(req, args):
	from hashlib import sha256
	return sha256(args).hexdigest()
