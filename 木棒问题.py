from time import time


def dfs(i, l):  # 切割木条(DFS:深度优先搜索)

    if lens[l] == 0:  # 当前木条刚好切完

        if not any(lens):  # 木条全部为0,即全部切下时成功返回
            return True
        i = 1
        while used[i]:
            i += 1
        used[i] += 1;
        lens[l + 1] -= sticks[i]  # 剪枝:该木棒当前最长,一定要用

        if dfs(i + 1, l + 1):
            return True

        used[i] = 0;
        lens[l + 1] += sticks[i]  # 若失败返回,则恢复递归前状态

    else:
        for j in range(i, num):
            if j > 0 and sticks[j] == sticks[j - 1] and (not used[j - 1]):
                continue
                # 剪枝:相同长度,若上一根未选用,
                # 这根同样无需考虑,直接跳过即可
            if (not used[j]) and lens[l] >= sticks[j]:
                # 剪枝(最基本):木棒未使用且小于长木条剩余长度
                lens[l] -= sticks[j];
                used[j] = 1

                if dfs(j, l):  # 递归,进一步搜索
                    return True

                lens[l] += sticks[j];
                used[j] = 0  # 若失败返回,则恢复递归前状态
                if sticks[j] == lens[l]:
                    break

    return False


def ts(l, s):  # 条数是否大于一条

    yz = []
    for i in range(l[0], s // 2 + 1):
        if s % i == 0:
            yz.append(i)
    return yz  # 找出并返回符合条件的因子,若无则返回空列表


if __name__ == '__main__':

    #print('请按提示输入相关信息,输入木棒数量为0时程序结束')

    num = int(input(''))
    while num:
        sticks = list(map(int, input().split()))
        # 读入木棒长度,并以列表形式储存
        time_begin = time()  # 开始计时
        sticks.sort(reverse=True)  # 剪枝:按降序排序

        _sum = sum(sticks)  # 木棒总长

        yz = ts(sticks, _sum)  # 按升序存储长木条可能的长度
        for len in yz:
            used = [0] * num  # 初始化used全部为0(未使用)
            # 放在for 循环下,每次重新尝试时重置
            lens = [len] * int(_sum / len)

            if dfs(0, 0):  # 调用递归函数
                time_end = time()
                print(len)
                break
        else:
            time_end = time()
            print(_sum)
            # 停止计时,并输出结果
        times = (time_end - time_begin) * 1000
        #print('耗时:', times, 'ms')
        num = int(input())
