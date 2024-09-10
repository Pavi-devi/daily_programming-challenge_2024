#daily_challenge_2024
arr = [1, 2, 4, 5]
n=len(arr)+1
def missingnum(arr,n):
    total = sum(arr)
    formula = n*(n+1)//2
    return formula-total
    
miss_num = missingnum(arr,n)
print(miss_num)
  
