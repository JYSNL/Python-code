class Pow_x:
    def __powxy__(self, x:float , y:int)->float:
        if y<0:
            y = -y
            return 1/self.help(x,y)
        return self.help(x,y)

    def help(self,x,y):
        if y==0:
            return 1
        if y%2==0:
            return self.help(x*x,y/2)
        return self.help(x*x,(y-1)/2)*x

if __name__=='__main__':
    x , y = int(input()) , int(input())
    powxy = Pow_x().__powxy__(x,y)
    print(powxy)