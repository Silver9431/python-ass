#Countdown Example: countdown(5) should return [5,4,3,2,1,0]
counts = 6
while counts > 0:
    print(counts)
    counts = counts -1
def my_fuction():
    numbers= [1,2,3,4,5]
    return numbers
print(my_fuction())    
    
#Print and Return Example: print_and_return([1,2]) should print 1 and return 2
def my_fuction():
    numbers= [1,2]
    return numbers
print(my_fuction())    

#First Plus Length Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
def first_length(list):
   
    return list[0] + len(list);
z= first_length ([1,2,3,4,5])
print (z);

#Values Greater than Second -values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
list = [1,2,3,4]
newlist= []
for x in list:
    if x>list[1]:
        newlist.append(x)
print (newlist)   

#length_and_value(6,2) should return [2,2,2,2,2,2]
a=[1,1,1,2,3,3,3] 
result = dict((i, a.count(i)) for i in a)
print (result)        
