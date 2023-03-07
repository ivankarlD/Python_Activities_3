length=int(input("Enter list lenght: "))
elements=input("Enter list elements: ")
listNum=[int(item) for item in elements.split(' ')]
listNum.sort()

def mean() :
    total=0 
    for item in listNum : 
        total=total+int(item)
    return int(total/length)

def median() :
    if length % 2 == 0:
        left = int(length / 2) - 1
        right = left + 1
        return int((listNum[left] + listNum[right])/2)
    else :
        return int(listNum[int(length/2)])

def mode() :
    mode=""
    counter={}
    for item in listNum :
        if item in counter : counter[item] += 1
        else : counter[item] = 0
    counter = dict(reversed(sorted(counter.items(), key=lambda item: item[1])))
    listCounter = list(counter)
    i = 1
    mode = f"{listCounter[0]}"
    while i < len(listCounter) :
        if counter[listCounter[0]] == counter[listCounter[i]] :
            mode += f", {listCounter[i]}"
            i += 1
        else : break
    return mode

print(f"MEAN: {mean()}")
print(f"MEDIAN: {median()}")
print(f"MODE: {mode()}")