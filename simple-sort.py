import random


def insertion_sort(items):
        """ Implementation of insertion sort """
        for i in range(1, len(items)):
                j = i
                while j &gt; 0 and items[j] &lt; items[j-1]:
                        items[j], items[j-1] = items[j-1], items[j]
                        j -= 1


random_items=[random.randint(-50,100) for c in range (10)]

print ('before: ', random_items)
insertion_sort(random_items)
print ('after: ',random_items)