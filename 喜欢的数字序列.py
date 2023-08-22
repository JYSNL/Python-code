arr_number = list(input())
len_arr = len(arr_number)
for i in range(0,len_arr):
    arr_number[i] = int(arr_number[i])
how_love = 99999
for i in range(0,len_arr-2):
    if abs((arr_number[i]*100 + arr_number[i+1]*10 + arr_number[i+2])-753) < how_love:
        how_love = abs((arr_number[i]*100 + arr_number[i+1]*10 + arr_number[i+2])-753)
print(how_love)