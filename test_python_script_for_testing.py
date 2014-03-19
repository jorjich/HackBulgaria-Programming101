from subprocess import call
import sys
import os

def main():
    if(len(sys.argv) == 2):
        file_directory = sys.argv[1]
        directory_content = os.listdir(file_directory) #sydyrjanieto na papkata
        for i in directory_content:
            if ("." not in i): #proverqvame, dali i e papka ili fail
                os.chdir(file_directory + "/" + i)
                print("Testing " + i + ":")
                call("python3.3 tests.py", shell = True)
                os.chdir(file_directory)
                print()
                print()
                print()
    elif(len(sys.argv)>2):
        return "Too many arguments given!"
    else:
        return "No arguments given!"

if __name__ == '__main__':
        main()
