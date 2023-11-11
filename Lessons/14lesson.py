lesson = "File handling"
"""
# CREATE A FILE
# To create non-existing file we use "x" mode
# Also, if the file IS FOUND then it returns an error
# ex: 
# f = open("myfile.txt", "x") # =>  x mode allows to create a 
                                # file if it does not exist, 
                                # otherwise it raises an error.
# if we don't want to get an error then we have to use os
# import os
# if os.path.exists("myfile.txt"):
#   print("The file exists")
# ===========================================================
# READ FILE
# When we open the file we have to always remember to close it
# If we don't close it then we can't open it again until we restart the program
# For reading the file we use 'r' mode
# Also, if the file is NOT FOUND then it returns an error

# 1. read()      => reads whole file (we also can specify how many characters to read)
# 2. readline    => reads only one line
# 3. readlines() => reads the file line by line (all lines)
# 4. loop through the file line by line

# ex:
#   f = open("myfile.txt", "r")
#       print(f.read())

# ===========================================================
# UPDATE A FILE
# To update an existing file, we use "a" mode or "w" mode
# --- (w)  write mode replaces the content of the file
# --- (a)  append mode appends the content to the end of the file
# ex:  
#   f = open("myfile.txt", "a")
#   f.write("Now the file has more content!")
#   ----------------------------
#   using keyword WITH
#   with open("myfile.txt", "a") as f:
#       f.write("Now the file has more content!")
# ===========================================================
# DELETE A FILE
# To delete a file, we use os.remove() function
# ex:
#   import os
#   os.remove("myfile.txt")

# ===========================================================
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# Combinations of modes:
"a+" - Read and Append - Opens a file for reading and appending, creates the file if it does not exist
"w+" - Write and Read - Opens a file for writing and reading, creates the file if it does not exist
"r+" - Read and Write - Opens a file for reading and writing, error if the file does not exist

# ===========================================================
# WORKING WITH DIRECTORIES and os
# import os
# os.mkdir("myfolder") # => creates a folder
# os.rmdir("myfolder") # => removes a folder
# os.rename("oldname", "newname") # => renames a folder
# os.getcwd() # => returns the current working directory
# os.path.exists("myfolder") # => checks if the folder exists
# os.path.isdir("myfolder") # => checks if the folder exists
# os.path.isfile("myfile.txt") # => checks if the file exists
# os.path.join("myfolder", "myfile.txt") # => joins the folder and the file
"""