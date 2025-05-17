import win32api

# Find files with .py extension in the current directory
files = win32api.FindFiles("*.py")

for file_info in files:
    # file_info is a tuple with details about the file
    # file_info[8] is the file name
    print(file_info[8])
