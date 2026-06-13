arr = [2,3,6,4,5]
n = 3
start=0
end=len(arr)-1
s = sorted(arr)
print(s)
i=0
while(start<=end):
    mid = start+end//2
    if arr[mid]==n:
        print("found",mid)
        break
    elif arr[mid]<n:
        start=mid+1
    else:
        end=mid-1