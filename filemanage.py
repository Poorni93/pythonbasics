"""file management """
file1 = open("file.txt")
#read the file
read_cont = file1.read()
print(read_cont)
#write the file 
file2 = open("file.txt","w")
file2.write("I write the second line")

#using with and us
with open("file.txt","r") as file3:
    readall = file3.read()
    print(readall)

#using append

file4 = open("file.txt","a")
file4.write("this code")
