def run(self) :
	self.process = subprocess.(self.cmd, stdout = self.outFile, stderr = self.errFile)
	while (self.process.() is None and self.timeout > 0) :
		time.(1)
		self.timeout -= 1
	if not self.timeout > 0 :
		self.process.()
		self.timed_out = True
	else :
		self.timed_out = False


def run(cmd, timeout_sec) :
	proc = subprocess.(shlex.split(cmd), stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	timeout = {"value" : False}
	timer = (timeout_sec, kill_proc, [proc, timeout])
	timer.()
	stdout, stderr = proc.()
	timer.()
	return proc., stdout.("utf-8"), stderr.("utf-8"), timeout ["value"]

