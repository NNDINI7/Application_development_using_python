def get_sum(a,b):
    return a+b

print(get_sum(10,50))

#using lambda function type 1
fun = lambda a, b: a+b
print(fun(100,200))

#using lambda function type 2
print((lambda a,b: a*b)(25,5))

#Applications of lambda function 
nums = [[10,100],[20,300],[15,400],[25,250]]
print(nums)
nums.sort()
print(nums)
print("_______________________________________________________________")

#reverse sort 
nums.sort(reverse= True)
print(nums)
print("_______________________________________________________________")

#sorting 2nd number
nums.sort(key= lambda x:x[1])#call function lambda and apply on 2nd value 
print(nums)  
print("_______________________________________________________________")

#sort according to multiplication of both the numbers 
nums.sort(key= lambda x:x[0]*x[1])
print(nums)  
print("_______________________________________________________________")
