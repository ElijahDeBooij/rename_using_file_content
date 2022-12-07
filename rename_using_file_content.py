# import required modules
import os
import time
# assign directory
directory = 'D:/folder/folder2/rename_using_file_content/source/'
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        # open file in "read" mode with UTF-8 encoding. change encoding if your file use different encoding replace UTF-8 with your encoding( for exampel ANSI)
        # here is an example: file = open(f, 'r',encoding="ANSI")
        file = open(f, 'r',encoding="utf-8")
        # this specifies which line is read.
        #  keep in mind that this is all contents of this line.
        # to modify which line is read change the number in the [] brackets from [2] to say [12] to read line 12
        line = file.readlines()[2]
        # closes the file
        file.close()
        # this removes ccharacters from the read line.
        # to add characters use ,'a','b' if you want to filter out more than 1 character use the later lines
        list_of_char = ['\n']
        mod_string1 = ''.join(filter(lambda k: k not in list_of_char, line))
        #this removes </title> from the string and replaces it with nothing.
        # effectivly removing </title> from the string 
        # to modify which string you remove form the read line
        # replace <title> with: 'your_string.' subsequent mod_strings are for further removing strings.
        mod_string2 = mod_string1.replace('</title>', '')
        #print(mod_string2)
        mod_string3 = mod_string2.replace('<title>', '')
        #print(mod_string3)
        mod_string4 = mod_string3.replace(',', ' ')
        #print(mod_string4)
        mod_string5 = mod_string4.replace(':', ' ')
        #mod_string6 = mod_string5.replace('\n', ' ')
        # set the output to the filterd string plus a chosen string in this case .html in order to preserver the orignal file extension.
        # replace this with your own note: this does not convert your files,
        # if you want to do that i reccomend pandoc
        output = mod_string5 + ".html"
        # print the final output.
        print(output)
        # renames the original file (f) to the final filterd string(output)
        os.rename(f,output)
        #this pause the program for 0.5 seconds this is not nessecary for operation on most (modern(as of 2022) computers.
        # any somewhat decent computer from 2015 or newer should work without any delay
        # older will probaly work good enough although this is untested.
        time.sleep(0.5)
