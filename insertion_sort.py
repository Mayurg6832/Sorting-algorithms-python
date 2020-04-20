def insertion(arr):
    for i in range(1,len(arr)):
        ele=arr[i]
        j=i-1
        while j>=0 and arr[j]>ele:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=ele
    
    return arr

lst=list(map(int,input().split()))
print(insertion(lst))