"""
Iterating over files.
"""

# Using readlines()
#  readlines creates a list of strings
#  that you can iterate over

datafile1 = open("the_idiot.txt", "rt")
#dat = datafile1.readlines()      # creates a list
#print("checking:", dat)

for line in datafile1.readlines():
    print(line)
    #print(line, end = "")     #To remove the extra blank lines
    #print(line[0:-1])         #To remove the extra blank lines

datafile1.close()

print("")
print("================================")
print("")

# Direct iteration
#  This is faster for large files,
#  as no list is created

datafile2 = open("the_idiot.txt", "rt")

for line in datafile2:
    print(line)

datafile2.close()
