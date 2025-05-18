'''

Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.

'''

def combine(arr1: list[int], arr2: list[int])-> list:
    i = j = 0
    combined_list = []
    while i < len(arr1) and j < len(arr2):
        
        if arr1[i] < arr2[j]:
            combined_list.append(arr1[i])
            i = i + 1
        elif arr2[j] < arr1[i]:
            combined_list.append(arr2[j])
            j = j + 1
    
    while i < len(arr1):
        combined_list.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        combined_list.append(arr2[j])
        j += 1
    
    return combined_list
        
    
print(combine([1,4,7,20],[3,5,6]))
