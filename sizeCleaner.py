import os
import shutil

# The directory that we are interested in cleaning up
source_Path=input("Enter Source Path \n")
dest_path=input("Enter Destination Path \n")
size=int(input("Enter size above which files should be copied in MB"))
# The threshold size, above which files would be copied.
tresSize = size*1000000

# All the file paths will be stored in this list
filesList= []

for path, subdirs, files in os.walk(source_Path): #Check all files even in sub directories and keep upending the list.
    for name in files:
        filesList.append(os.path.join(path, name))

for i in filesList:
    # Getting the size in a variable
    fileSize = os.path.getsize(str(i))

    # Print the files that meet the condition
    if int(fileSize) >= tresSize:
        print("The File: " + str(i) + " is: " + str(fileSize) + " Bytes" )
        if(os.access(str(i),os.X_OK and os.W_OK)): #Ignore Read Only files
            print("Now copying the file mentioned above")
            shutil.move(str(i), dest_path) #Path you want to copy it to
            print("Copy done")
        else:
            print(" But Could not copy as it's Read Only")
