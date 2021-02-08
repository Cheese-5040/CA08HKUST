import random
# bubble sort
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                #if next item is larger than init item in mark, swap them 
                temp = items[j+1]
                items[j+1] = items[j]
                items[j] = temp
                # items[j], items[j+1]=items[j+1],items[j]



# insertion sort
def insertion_sort(items):
    for i in range(1, len(items)): 
  
        key = items[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < items[j] : 
                items[j + 1] = items[j] 
                j -= 1
        items[j + 1] = key 



random_items=[]
def randomise(number):
    for x in range(number):
        random_items.append(random.randint(-50,100))
    print(random_items)

randomise(10)
bubble_sort(random_items)
print("bubble sort: ", random_items)


randomise(10)
insertion_sort(random_items)
print("insertion sort: ", random_items)
