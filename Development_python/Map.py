#It is process where we can apply iterator on any function and return corresponding results
nums = [1,2,3,4,5,6,7,8,9,10]
# squares = []
# for i in nums:
#     squares.append(i**2)
squares = list(map(lambda x:x**2,nums)) #used to retrieve the numbers of that type and list print those numbers 
print(squares)