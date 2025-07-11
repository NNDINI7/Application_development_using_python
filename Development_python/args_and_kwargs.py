
#using *args 
def get_sum(*args): #args can add any number of parameters as a tuple to perevent overfitting 
    print(type(args))
    print(args)
    
    sum = 0
    for i in args:
        sum += i #sum = sum + i 
    return sum 
print(get_sum(10,20)) #0 = 0+10 = 10 , 10 = 10+20 = 30
print(get_sum(10,20,30))
print(get_sum(10,20,30,40,50))

print("**************************************************************************")
#using **kwargs
def print_info(val1, val2, name , city ):
    print(val1-val2)
    print(name)
    print(city)

print_info(10,20,"Shree","Nagpur") #unnamed args / #positional args 
print("**************************************************************************")

print_info(val2=300 , val1=100 ,  name="Shivansh" , city="Nagpur") #named args / #keyword args , parameters are passed using key element , sequence doesnot matter.
print("**************************************************************************")

print_info(10,20, city="Mumbai" , name="ABC") #potitional args cannot appear after keyword args 
print("**************************************************************************")

def info(*args,**kwargs ):
    print(type(args), args)
    print(type(kwargs), kwargs)
    for k,v in kwargs.items():
        print(k,v)

info(100,10,"a","banglore")
info(city = "mumbai" , val2 = 20 , val1 = 10 , name ="R")


