#Bubble Sorting

num = int(input("How many number you want to enter??:"))
list1 = [ int(input("Enter number:")) for x in range(num)] #list comphansaion
# list1=[23,0,25,12,4]

print("unsorted list is:",list1)
for j in range (len(list1) -1):
    for i in range (len(list1)-1):
        if list1[i] > list1[i+1]:
            list1[i],list1[i+1] = list1[i+1],list1[i]
            print(list1)
        else:
            print(list1)
            
print(list1)
 
 #Selection Sort

list1 = [56,3,2,9,78,6,0]
print("Unsorted list1",list1)

for i in range(len(list1) -1):
    min_val = min(list1[i:])
    min_ind = list1.index(min_val,i)
    if list1[i] != list1[min_ind]:
        list1[i],list1[min_ind] = list1[min_ind],list1[i]   # swap the values
    print(list1)
print(list1)

#Quick Sort
#to get the correct position of the pivot element
import random
def pivot_place(list1,first,last):
    rindex = random.randint(first,last)
    list1[rindex],list1[last] = list1[last],list1[rindex]
    pivot = list1[last]        # When pivot are last than swap pivot to left
    left = first
    right = last-1

    while True:
        while left<=right and list1[left]  <= pivot:
            left = left+1
        while left<=right and list1[right] >=pivot:
            right = right-1
        if right<left:
            break
        else:
            list1[left],list1[right] = list1[right],list1[left]
    list1[last],list1[left] = list1[left],list1[last]
    #swap last to left and return left
    return left

def quicksort(list1,first,last):
    if first<last:
        p = pivot_place(list1,first,last)
        quicksort(list1,first,p-1)
        quicksort(list1,p+1,last)


#main
list1 = [6,29,93,31,44]
print("Unsorted list:",list1)
n = len(list1)
quicksort(list1,0,n-1)
print("Sorted list is :",list1)

#to get the correct position of the pivot element

def pivot_place(list1,first,last):
    
    pivot = list1[first]        # When pivot are first than swap pivot to right
    left = first+1
    right = last

    while True:
        while left<=right and list1[left]  <= pivot:
            left = left+1
        while left<=right and list1[right] >=pivot:
            right = right-1
        if right<left:
            break
        else:
            list1[left],list1[right] = list1[right],list1[left]
    list1[first],list1[right] = list1[right],list1[first]
    return right

def quicksort(list1,first,last):
    if first<last:
        p = pivot_place(list1,first,last)
        quicksort(list1,first,p-1)
        quicksort(list1,p+1,last)


#main
list1 = [6,29,93,31,44]
print("Unsorted list:",list1)
n = len(list1)
quicksort(list1,0,n-1)
print("Sorted list is :",list1)

