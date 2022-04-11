"""
my_list = [9,1,0,2,8,6,7,15]
print('original list:', my_list)
my_list.insert(-20, 'one')
print('after insert:', my_list)

"""
"""
my_list = [9,1,0,2,8,6,7,15]
#my_list = ['Sunday','Monday','Thursday']
print('original list:', my_list)
my_list.sort()
print('after sort:', my_list)
"""
"""
my_list = [9,1,0,2,8,6,8,7,15]

print('original list:', my_list)
my_list.remove(8)
my_list.remove(8) #removes the chosen number
my_list.reverse() #reverse the list 

print('after sort:', my_list)
"""
"""
my_list = [9,1,0,2,8,6,8,7,15]

print('original list:', my_list)

maxv = max(my_list)
minv = min(my_list)

print('maximum is:', maxv)
print('minimum is:', minv)
"""
"""
lst1 = [1,2,3,4,5]
lst2 = lst1

lst1[0] = 99

print(lst1)
print(lst2)
"""
"""
lst1 = [1,2,3,4,5]
lst2 = lst1
lst3 = []
for item in lst1:
    lst3.append(item)
lst4 = [] + lst1
lst5 = lst1[:]

print("list1",lst1)
print("list2",lst2)
print("list3",lst3)
print("list4",lst4)
print("list5",lst5)
lst1[0] = 99

print("list1",lst1)
print("list2",lst2)
print("list3",lst3)
print("list4",lst4)
print("list5",lst5)
"""
"""
numbers = [10,20,30,40,50]
print(numbers)

total=0
for value in numbers:
    total += value

print(total) 
average = total/len(numbers)
print(average)
"""
"""
lst1 = ['one','two','three']
outfile = open('myfile','w')
outfile.writelines(lst1)
outfile.close()
"""

"""
lst1 = ['one','two','three']
outfile = open('myfile','w')

for item in lst1:
    outfile.write(item+'\n')

outfile.close()
"""





names = [['Joe', 'Kim'],['Sam','Sue'],['Kelly','Kris']]
print(names)
