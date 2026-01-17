'''In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
'''
def main():
   File_Name=input(" File Name: ")
   extension(File_Name)
   print(extension(File_Name))
def extension(fn):
    if fn.endswith(".gif"):
        return "image/gif"
    elif fn.endswith(".jpg"):
        return "image/jpg"
    elif fn.endswith(".jpeg"):
        return "image/jpeg"
    elif fn.endswith(".png"):
        return "image/png"
    elif fn.endswith(".pdf"):
        return "application/pdf"
    elif fn.endswith(".txt"):
        return "text/plain"
    elif fn.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"
main()
