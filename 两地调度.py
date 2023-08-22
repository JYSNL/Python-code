def twoCitySchedCost(costs: List[List[int]]):
    f = lambda x: abs(x[0] - x[1])
    costs = sorted(costs, key=f, reverse=True)
    res = 0
    a = b = len(costs) // 2
    for i in costs:
        if b and i[0] > i[1]:
            res += i[1]
            b -= 1
        elif a and i[0] < i[1]:
            res += i[0]
            a -= 1
        elif not a and b:
            res += i[1]
            b -= 1
        else:
            res += i[0]
            a -= 1
    return res
