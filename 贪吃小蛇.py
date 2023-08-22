N = int(input())    #N存储总共的蛇蛇数量
snakes = list(input().split(' '))
for i in range(0,len(snakes)):
    snakes[i] = int(snakes[i])
snakes.sort()
hei_snakes = []
hei_snakes.append(snakes[0])
for i in range(1,len(snakes)):
    hei_snakes.append(hei_snakes[i-1]+snakes[i])
snakes.sort(reverse=True)
hei_snakes.sort(reverse=True)
temp = 0
#将蛇的重量从高到低排序，然后将大重量吃掉前面所有小重量排序
#如果当前吃掉所有小蛇的蛇*2可以吃掉下一条蛇，则没问题
#如果不能吃，则退出循环
for i in range(1,len(snakes)):
    if hei_snakes[i]*2>=snakes[i-1]:
        temp = i+1
        continue
    else:
        temp = i
        break
print(temp)