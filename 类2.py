class animal:
    def __init__(self,name,size,color):
        self.name = name
        self.size = size
        self.color = color
        print('状态已完成！')
    def Showname(self):
        print('该动物的名称为：',self.name)
    def __del__(self):
        class_name = self.__class__.__name__
        print (class_name,'销毁')


class eat(animal):
    def start(self,eat):
        self.eat = eat
    def Eatwhat(self):
        print(self.name,'吃',self.eat)

def main():

    x = animal('mouse','small','white')
    x.Showname()
    del x
    y = eat('horse','medium','brown')
    y.start('weed')
    y.Eatwhat()
    del y

if __name__ == '__main__':
    main()
