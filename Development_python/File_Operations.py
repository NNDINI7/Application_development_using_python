
# FILE OPEARTIONS

# write into the file 
with open("abc.txt","w") as f:
    f.write("Hello World ! \n") 
    f.write("Good Morning ! \n") 
    f.write("Happy Day ! \n") 
    print("___________________________")
  
# read the file   
with open("abc.txt","r") as f:
    print(f.read()) # reads whole file 
    print(f.readline()) # reads single line 
    print("___________________________")

# append contents at the end of file 
with open("abc.txt","a") as f:
    f.write("Appended line 1 \n") 
    f.write("Appended line 2 \n") 
    f.write("Appended line 3 \n") 
  
with open("abc.txt","r") as f:
    print(f.read()) # reads whole file 
    print(f.readline()) # reads single line 
    print("___________________________")

# + : both read and write allowed 

# r+ : 
#  - if file not exists throws error 
#  - if file exists , the file pointer is set to SOF and then read/write
with open("abc.txt","r+") as f:
    print(f.read())

with open("abc.txt","r+") as f:
    f.write("####")
    print(f.read())

# w+ :
# - if file does not exists then create and perform read/write 
# - if file exists , it deletes existing file contents and then read/write 


# a+ :
# - if file does not exists then create and perform read/write 
# - if file exists , the file pointer is set to EOF and then read/write 





