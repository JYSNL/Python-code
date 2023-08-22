def move(n,a,b,c):
    if n==1:
        print(a+'->'+c)
        return
    move(n-1,a,c,b)  #把n-1个盘子借助c由a移动到b
    move(1,a,b,c)    #剩余一个盘子从a到c
    move(n-1,b,a,c)  #再把n-1个盘子借助a由b移动到c

n=input('').split( )
n1=int(n[0])
a=str(n[1])
b=str(n[2])
c=str(n[3])
move(n1,a,b,c)

