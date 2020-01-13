import re
import subprocess
import sys

#lof = list of file
#is_exist return string is empty or not
#save_the_all_lof -> return list matched with inp(input)
#print_fille -> print lof's 10 element

def is_exist(string):
    if(string != None):
        return 1
    else:
        return 0

def save_the_all_lof(inp):
    temp = []
    input_value = re.compile(inp)
    for name in lof:
        if (is_exist(input_value.search(name.split('/')[-1]))):
            temp.append(name)
    return temp

def print_file():
    print("------------------------------")
    for i in range(len(lof)):
        if(i == 10):
            break
        else:
            print "{}\t({})".format(lof[i],i+1)

Parent_directory = subprocess.check_output("git rev-parse --show-toplevel".split()).strip()
lof = subprocess.check_output(("git ls-files "+Parent_directory).split()).strip().split()
lof = save_the_all_lof(sys.argv[1])

while 1:
    #Only one file is searched
    if (len(lof) == 1):
        subprocess.call(["vi",lof[0]])
        break 
     
    #No file is searched
    elif(len(lof) == 0):
        print("There is no file\n")
        break

    #More than 2 file are searched
    else: 
        print_file()
        insert =raw_input("Enter file shorcut (shown on the right) or keyword to further refine the search:\n")
        check = insert.isdigit()
        
        #If insert is a number
        if(check and 0<int(insert) and int(insert) < 11):
            subprocess.call(["vi",lof[int(insert) -1]])
            break
        
        #If insert is a string
        else:
            lof = save_the_all_lof(insert) 
