def removeKdigits(num, k):
    stack = []
    remain = len(num) - k
    for digit in num:
        while k and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    return ''.join(stack[:remain]).lstrip('0') or '0'
k = int(input(''))
s = input('')
num = str(s)
des = removeKdigits(num,k)
print(des)

