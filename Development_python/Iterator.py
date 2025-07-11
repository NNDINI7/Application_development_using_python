
#ITERATOR 
num = [10,20,30,40,50]
for n in num:
    print(n,end = " ")
print("\n--------------------------")


#custom iterator class 
from random import random , randint , uniform 
class MyRandom:
    def __init__(self,low,high,count):
        self.low = low
        self.high = high 
        self.count = count
        self.current = 0 #counter for current iteration 
    
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.current < self.count:
            self.current += 1
            return random()*(self.high-self.low)+self.low
        else:
            raise StopIteration

for r in MyRandom(50,70,10): #low,high,count
    print(r, end=" ")

