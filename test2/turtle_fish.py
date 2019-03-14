import random

class BaseAnimal():
    def __init__(self):
        self.x=random.randint(0,9)
        self.y=random.randint(0,9)

    def is_vaild(self,value):
        if value<0:
            return abs(value)
        if value>9:
            return 9-(value-9)
        return value

class Turtle(BaseAnimal):
    def __init__(self):
        super().__init__()
        self.power=100

    def move(self):
        move_skill = [-1, 1, 0, -2, 2]
        new_x = self.x + random.choice(move_skill)
        new_y = self.y + random.choice(move_skill)
        self.x = self.is_vaild(new_x)
        self.y = self.is_vaild(new_y)
        self.power-=1

    def eat(self):
        self.power+=20
        if self.power>=200:
            self.power=200

class Fish(BaseAnimal):
    def move(self):
        move_skill = [-1, 1, 0]
        new_x = self.x + random.choice(move_skill)
        new_y = self.y + random.choice(move_skill)
        self.x = self.is_vaild(new_x)
        self.y = self.is_vaild(new_y)


def main():
    t1=Turtle()
    fishs=[Fish() for i in range(10)]
    while True:
        if t1.power<=0:
            print('乌龟死亡，游戏结束！！！！')
            break
        elif len(fishs)==0:
            print('鱼被吃光，游戏结束！！！！')
            break
        else:
            t1.move()
            for fish in fishs:
                fish.move()
                if t1.x==fish.x and t1.y==fish.y:
                    t1.eat()
                    fishs.remove(fish)
                    print('鱼被吃掉了')
                    print('乌龟最新体力: %s' % (t1.power))
            else:
                print('乌龟没有吃到鱼，最新体力为: %s' % (t1.power))
if __name__=='__main__':
    main()