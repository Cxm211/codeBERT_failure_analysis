def touch(file_name) :
	if not os.path.***exists***(file_name) :
		return
	try :
		os.***utime***(file_name, None)
	except Exception :
		***open***(file_name, 'a').close()


def touch(fname, mode = 0o666, dir_fd = None, ** kwargs) :
	flags = os.O_CREAT | os.O_APPEND
	with os.***fdopen***(os.***open***(fname, flags = flags, mode = mode, dir_fd = dir_fd)) as f :
		os.***utime***(f.fileno() if os.utime in os.***supports_fd*** else fname,
		dir_fd = None if os.***supports_fd*** else dir_fd, ** kwargs)

