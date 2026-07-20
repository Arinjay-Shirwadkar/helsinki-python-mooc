# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.sum=0
        self.averag=0
        self.nums=0

    def add_number(self, number:int):
        self.nums+=1
        self.sum+=number
        self.averag = (self.sum)/self.nums

    def count_numbers(self):
        return self.nums
    
    def get_sum(self):
        return self.sum
    
    def average(self):
        return self.averag

print("Please type in integer numbers:")
num = int(input())

stats = NumberStats()
even = NumberStats()
odd = NumberStats()

while(num!=-1):
    stats.add_number(num)
    
    if num%2==0:
        even.add_number(num)
    else:
        odd.add_number(num)
    num = int(input())
print('Sum of numbers:',stats.get_sum())
print('Mean of numbers:',stats.average())
print('Sum of even numbers:',even.get_sum())
print('Sum of odd numbers:',odd.get_sum())