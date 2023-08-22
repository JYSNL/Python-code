import random
import string
import time
i = 3000
file = open('1.txt','w')
start = time.time()
while(i):
    i -= 1
    str1 = random.sample(string.ascii_letters + string.digits,random.choice(range(1,90)))
    str2 = ''.join(str1)
    file.write(str2+'\n')
end = time.time()
print("运行时间：{}".format(end-start))
file.close()