def countSort(arr):
	count=[0]*(max(arr)+1)
	ans=[]
	for i in arr:
		count[i]+=1

	for i in range(len(count)):
		ans+=([i]*count[i])

	return ans

arr=list(map(int,input().split()))
print(countSort(arr))
