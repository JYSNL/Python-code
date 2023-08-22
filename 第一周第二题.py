arr = input("")
brr = list(arr)
print(len(arr))
for i in range(0,len(arr)-1):
    for j in range(i+1 , len(arr)):
        if brr[i] > brr[j]:
            temp = brr[i]
            brr[i] = brr[j]
            brr[j] = temp
crr = "".join(brr)
print(crr)
