filename=input("enter the file name to open:")
try:
    with open(filename,"r")as f:
        content=f.read()
        print("file content:\n",content)
except FileNotFoundError:
        print("FileNotFoundError:the file'{filename}'does not exist.")
