from vpython import *
import random

canvas(width=750,height=420,background=color.black)



def bubble_sort():
    for i in range(len(l2)):
        for j in range(len(l2) - i - 1):
            # Compare the adjacent elements
            if l2[j].height > l2[j + 1].height:
                # Swap the elements
                l2[j].color=color.red
                l2[j+1].color=color.green
                sleep(0.01)
                l2[j].height, l2[j+1].height = l2[j + 1].height, l2[j].height
                l2[j].pos.y, l2[j+1].pos.y = l2[j + 1].pos.y, l2[j].pos.y
                l2[j].color=color.white
                l2[j+1].color=color.white
        l2[len(l2)-1-i].color=color.blue

def selection_sort():
    for i in range(len(l2) - 1):
        min_index = i
        for j in range(i + 1, len(l2)):
            if l2[j].height < l2[min_index].height:
                
                min_index = j
        if min_index != i:
            l2[i].color=color.red
            l2[min_index].color=color.red
            sleep(0.2)
            l2[i].height, l2[min_index].height = l2[min_index].height, l2[i].height
            l2[i].pos.y, l2[min_index].pos.y = l2[min_index].pos.y, l2[i].pos.y
            l2[i].color=color.white
            l2[min_index].color=color.white
        l2[i].color=color.blue

def insertion_sort():
    l2[0].color=color.blue
    for i in range(1, len(l2)):
        j = i
        l2[i].color=color.blue
        while j > 0 and l2[j].height < l2[j-1].height:
            l2[j].color=color.red
            sleep(0.01)
            l2[j].height, l2[j-1].height = l2[j-1].height, l2[j].height
            l2[j].pos.y, l2[j-1].pos.y = l2[j-1].pos.y, l2[j].pos.y
            l2[j].color=color.blue
            j -= 1

print("Select 1 for bubble sort, 2 for insertion sort, 3 for selection sort")
x=int(input())


l=[int(random.randint(1,100)) for _ in range(1,140)] 
l2=[]
for i in range(len(l)):
    l2.append(box(length=0.8,width=1,height=l[i],pos=vector(i-70,l[i]/2-40,0)))

if(x==1):
    bubble_sort()
elif(x==2):
    selection_sort()
else:
    insertion_sort()

# insertion_sort() 
# selection_sort()
# bubble_sort()
