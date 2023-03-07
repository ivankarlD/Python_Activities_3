length=int(input("Enter list lenght: "))
elements=input("Enter list elements: ")
list=[int(item) for item in elements.split(' ')]
list.sort()

def mean() :
    total=0 
    for item in list : 
        total=total+int(item)
    return int(total/length)

def median() :
    if length % 2 == 0:
        left = int(length / 2) - 1
        right = left + 1
        return int((list[left] + list[right])/2)
    else :
        return int(list[int(length/2)])

def mode() :
    

print(f"MEAN: {mean()}")
print(f"MEDIAN: {median()}")