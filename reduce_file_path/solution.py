def reduce_file_path(path):
	is_it = True
	final_path = ""
	for i in path:
		if ( i != "/"):
			is_it = False
	if (is_it):
		return "/"
	else:
		new_path = path.replace("//", "/")
		folders = new_path.split("/")
		for i in range(1, len(folders)):
			if(folders[i] == "."):
				folders[i] = folders[i].replace(".", "")
			if(folders[i] == ".."):
				folders[i] = folders[i].replace("..", "")
				folders[i-1] = folders[i-1].replace(folders[i-1], "")
		for i in folders:
			if (i != ""):
				final_path += "/" + i
		if(final_path == ""):
			return "/"
		else:
			return final_path


def main():
	print(reduce_file_path("/"))
	print(reduce_file_path("/srv/../"))
	print(reduce_file_path("/srv/www/htdocs/wtf/"))
	print(reduce_file_path("/srv/www/htdocs/wtf"))
	print(reduce_file_path("/srv/./././././"))
	print(reduce_file_path("/etc//wtf/"))
	print(reduce_file_path("/etc/../etc/../etc/../"))
	print(reduce_file_path("///////////////"))
	print(reduce_file_path("/../"))
if __name__ == '__main__':
		main()