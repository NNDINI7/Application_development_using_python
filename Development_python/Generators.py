num = range(1,1000000)#range is generator that generates number at a time when needed using for loop. generate numbers one by one.
print(type(num),num)
for i in range(1,1000000):
    pass

print(num)
print("-----------------------------------------------------")

#function used to know the size of variable 
n = 100
print(type(n), n.__sizeof__()) #in bytes 
print("-----------------------------------------------------")

#INFINITE NUMBER GENERATOR 
def infinite_gen():
    i = 0 
    while True:
        i += 1
        yield(i)

fun = infinite_gen()
for _ in range(100):
    print(next(fun),end = " ")
print("-----------------------------------------------------")

for i in range (1,11,2):
    print(i, end=" ")

#for i in range(0,2,0.1):
#    print(i,ends=" ") EEROR
print("-----------------------------------------------------")

#make use of generator for above error 
def myrange(start,end,step):
    i = start
    while i<end:
        yield(i)
        i += step

for i in myrange(0,2,0.1):
    print("{:.2f}".format(i),end=" ") #upto 2 decimals 

print("*********************************************************")
