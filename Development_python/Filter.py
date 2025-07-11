nums = [1,2,3,4,5,6,7,8,9,10]
#odds = []
#for i in nums:
# if i % 2 !=0:
#     odds.append(i)

odd = list(filter(lambda x: x%2!=0,nums))
print(odd)

#use of ternary operator if else in one single line 
result = list(map(lambda x: 0 if x%2!=0 else x**2 , nums))
print(result)