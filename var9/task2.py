import dis
def foo():
	return ((b | (750 * b)) * (h & c)) | d
dis.dis(foo)
