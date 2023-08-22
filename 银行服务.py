rest = int(input('请输入余额为:'))
n=0
def quqian():
    qu=int(input('您要取的金额为：'))
    global rest
    if qu > rest:
        print('余额不足请充值')
    else:
        rest=rest-qu
        print('请稍等...', '余额为', rest)
    global n
    n+=1
def fuwu():
    print('请输入您需要的服务（1：取钱）/:2：存钱）')
    service = input('请输入您需要的服务:')
    jinxing(service)
def cunqian():
    global rest
    cun = int(input('您要存的金额为:'))
    rest=rest+cun
    print('您的余额为', rest)
    global n
    n+=1
def jinxing(service):
    if service == '1':
        quqian()
    elif service == '2':
        cunqian()
    else:
        print('暂无您需要的服务')
    print('请问需要进行其他服务吗？')
    service=input('请输入服务类型（不需要请输入0）：')
    if service == '1' or service == '2':
        jinxing(service)
    else:
        print('再见！')
pwd='542968'
cipher=input('请输入你的密码：')
if cipher==pwd:
    print('密码正确！')
    fuwu()
else:
    for i in range(2):
        print('密码错误，请重新输入密码：您还有'+str(2-i)+'次机会输入密码')
        cipher1=input()
        if cipher1==pwd:
            print('密码正确!')
            fuwu()
            break
        else:
            continue
    print('三次密码输入错误，请到前台申请服务！')
print('共完成了'+str(n),'次银行交易')