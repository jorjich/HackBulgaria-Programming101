import sys

from random import randint


def concat_files(*args):
	if len(sys.argv) > 1:
		mega = "MEGATRON.txt"
		fmega = open(mega, "a")
		for i in range(1, len(sys.argv)):
			fname = sys.argv[i]
			file = open(fname, "r")
			content = file.read()
			fmega.write("".join(content))
			file.close()
		fmega.close()
		return content
	else:
		return "No given arguments!"


def main():
	return concat_files(sys.argv)


if __name__ == '__main__':
	main()
