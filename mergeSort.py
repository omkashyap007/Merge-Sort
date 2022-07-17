"""
Level of sorting algorithm -: 2

[   1 is good,
    2 is better ,
    3 is best,
]

Type of algorithm -: Divide and conquer

Space complexity -: O(N)

Time complexity -: O(NlogN)

Stability -: stable

Good / bad  -: good


"""



arr = [ 7,6,8,16,1,4,3,9,2,11,19,20,17,12,15,14,10,13,18]

def mergeSort(arr) :
    if len(arr) > 1 :
        
        # if the length of the array is greater than 1 , shred the array until its lenght reaches less than 1 or 1 
        
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        
        # apply mergesort on both the arrays found after divinding theminto two.
        
        mergeSort(left)
        mergeSort(right)
        
        # now compare the elemenmts and then start appending to the array to get  the final sorted output . 
        i = j = k  = 0
        while i<len(left) and j<len(right) :
            if left[i] < right[j] :
                arr[k] = left[i]
                i+=1
            else :
                arr[k] = right[j]
                j+=1
            k+=1
            
        while i <len(left) :
            arr[k] = left[i]
            i+=1
            k+=1
        while j <len(right) :
            arr[k] = right[j]
            j+=1
            k+=1
            
    return arr    
arr = [80, 39, 4, 30, 50, 70, 47, 7, 63, 36, 4, 47, 47, 14, 34, 32, 42, 78, 44, 86, 56, 5, 54, 83, 91, 66, 49, 99, 47, 31]
print(mergeSort(arr))

