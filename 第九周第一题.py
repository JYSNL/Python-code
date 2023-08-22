class Solution(object):
    def intToRoman( self,num):
        """
        :type num: int
        :rtype: str
        """
        m = [
            ['', 'M', 'MM', 'MMM'],
            ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
            ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
            ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        ]  # 第一维数组分别对应千百十个，当对应位置没有值时，空字符与其对应。后面的十个字符一一对应每个位置的“一到十”

        d = [1000, 100, 10, 1]  # 每个位置的除数

        r = ''  # 初始化结果

        for k, v in enumerate(d):  # 对每一个位置进行判断，看看是否存在当前位置的值
            r += m[k][int(num / v)]  # 如果存在则对字符进行相加
            num = num % v  # 对下一级进行判断

        return r

if __name__ == '__main__':
    x = int(input(''))
    xnum = Solution().intToRoman(num=x)
    print(xnum)
