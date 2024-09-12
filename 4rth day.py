def next_gap(gap):
    if gap <= 1:
        return 0
    return (gap // 2) + (gap % 2)

def merge_in_place(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    gap = next_gap(m + n)
    
    while gap > 0:
        
        i = 0
        while i + gap < m:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1
        
       
        j = gap - m if gap > m else 0
        while i < m and j < n:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1

        
        j = 0
        while j + gap < n:
            if arr2[j] > arr2[j + gap]:
                arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
            j += 1

        
        gap = next_gap(gap)


arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merge_in_place(arr1, arr2)
print("Merged arr1:", arr1)
print("Merged arr2:", arr2)
