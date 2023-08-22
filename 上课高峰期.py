nck = list(input().split(' '))        #输入的所有人数，电梯承载量，人的忍耐度
N = int(nck[0])
C = int(nck[1])
K = int(nck[2])
arrive_time = []
#对每个人的到达时间进行输入并存储在列表中
for i in range(0,N):
    arrive_time.append(int(input()))
arrive_time.sort()          #从小到大排序
count = 0           #需要的电梯数
number_ele = 1   #电梯里的人
temp = arrive_time[0]
#每一次都从第一个人开始，往后看是否超过等待时间与电梯内容量是否足够进行判断
for i in range(1,N):
    if(arrive_time[i]-temp<=K and number_ele<C):
        number_ele+=1
    else:
        count+=1
        number_ele = 1
        temp = arrive_time[i]
count+=1
print(count)