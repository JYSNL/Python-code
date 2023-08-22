#初始化
Initial_Arr = input().split(' ')
n = int(Initial_Arr[0])
m = int(Initial_Arr[1])
need_first = int(Initial_Arr[2])
need_second = int(Initial_Arr[3])

#记录每支队伍是否完成匹配
Whether_Grouped = [0 for i in range(0,n)]

#记录下每支队伍中的选手的职业
Group = []

#记录下人员的总和
all_people = 0

#将n组队员输入
for i in range(0,n):
    People = []
    s = input().split(' ')
    for j in range(1,len(s)):
        People.append(int(s[j]))
    all_people += len(s)-1
    Group.append(People)

#先排除一支队伍中有两名及以上必须队员的
f=0
s=0
for i in range(0,n):
    for j in Group[i]:
        if j==need_first:
            f+=1
        elif j==need_second:
            s+=1
    if f==2 or s==2:
        Whether_Grouped[i]=1
    s = 0
    f = 0

#两位必要的成员是否已经加入匹配队伍
whether_first = 0
whether_second = 0

#Get_Group记录当前能匹配的队伍，id存储其队伍id
Get_Group = []
id = []

while(all_people>=m):
    #先确保组队人中有需要的两个人
    for i in range(0,n):
        if need_first in Group[i] and whether_first == 0 and len(Get_Group)+len(Group[i])<=m and Whether_Grouped[i]==0 and need_first not in Get_Group:
            whether_first = 1
            Whether_Grouped[i]=1
            for j in Group[i]:
                Get_Group.append(j)
            id.append(i)
            all_people-=len(Group[i])
        elif need_second in Group[i] and whether_second == 0 and len(Get_Group)+len(Group[i])<=m and Whether_Grouped[i]==0 and need_second not in Get_Group:
            whether_second = 1
            Whether_Grouped[i]=1
            for j in Group[i]:
                Get_Group.append(j)
            id.append(i)
            all_people-=len(Group[i])
    #再从剩下的队伍中去寻找
    for i in range(0,n):
        if len(Group[i])+len(Get_Group)<=m and Whether_Grouped[i]==0 and need_first not in Group[i] and need_second not in Group[i]:
            Whether_Grouped[i]=1
            for j in Group[i]:
                Get_Group.append(j)
            id.append(i)
            all_people-=len(Group[i])
    if len(Get_Group)==m:
        for idx in id:
            print(idx+1,end=' ')
        print()
        Get_Group = []
        id = []
        whether_first = 0
        whether_second = 0
    else:
        break




