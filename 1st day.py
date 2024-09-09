def sortof012(arr):
  left = 0
  mid = 0
  right= len(arr)-1

  while mid <= right :
    if arr[mid]== 0:
      arr[left],arr[mid]= arr[mid],arr[left]
      left +=1
      mid +=1
    elif arr[mid]==1:
      mid +=1
    else:
      arr[right],arr[mid]=arr[mid],arr[right]
      right-=1

arr = [0, 1, 2, 1, 0, 2, 1, 0]
sortof012(arr)
print(arr)
