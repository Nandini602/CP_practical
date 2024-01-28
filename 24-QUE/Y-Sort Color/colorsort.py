

def ColorSort(array): 
    for i in range(0,len(array)-1):
        for j in range(len(array)-1): 
            if(array[j]>array[j+1]):
                temp = array[j]
                array[j] = array[j+1] 
                array[j+1] = temp 

    return  array

array = list(map(int, input("Enter elements: ").split())) 
print(array) 
ColorSort(array) 
print(array)


