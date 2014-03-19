import sys

def main():
    if( len(sys.argv) > 1):
        file1 = sys.argv[1]
        file = open(file1, "r")
        content = file.read()
        file.close()
        return (content)
    else:
        return ("No arguments given")

if __name__ == '__main__':
        main()
