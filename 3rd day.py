arr = [3, 1, 3, 4, 2]
n=len(arr)
def duplicates(arr,n):
    res = set()
    for i in range(n):
        arr[i]+= 1
    for i in arr:
        if arr[abs(i)-1]<0:
            res.add(abs(i)-1)
            
        else:
            arr[abs(i)-1]*=-1
            
    if len(res)==0:
        return [-1]
    return sorted(res)  
    
arrdupli = duplicates(arr,n)

print(arrdupli)
