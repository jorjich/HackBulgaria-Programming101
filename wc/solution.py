import sys


def wc(*args):

	if len(sys.argv) == 3:
		story = sys.argv[2]
		fname = open(story, "r")

		word = sys.argv[1]
		if word == "chars":
			content = fname.read()
			fname.close()
			return len(content)
		elif word == "words":
			content = fname.read()
			new = []
			for item in content.split("\n"):
				if item != '':
					new += item.split(" ")
			fname.close()
			return len(new)
		elif word == "lines":
			count = 0
			content = fname.read()
			content = content.split("\n")
			for line in content:
				count += 1
			fname.close()
			return count - 1
	else:
		return "No given arguments!"


def main():
	return wc(sys.argv)


if __name__ == '__main__':
	main()
