def swap(ele1_index,ele2_index,array):
    temp2 = array[ele1_index]
    temp1 = array[ele2_index]
    array[ele1_index] = temp1
    array[ele2_index] = temp2
    
def bbbs(array):
    for i in range(len(array)-1):
        for x in range(len(array)-1):
            if array[x] > array[x+1]:
                swap(x,x+1,array)
        print(array)
    return(array)
        


