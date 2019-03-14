import time as t

class Mytimer():
    def __init__(self):
        self.unit=['年','月','天','小时','分钟','秒','']
        self.prompt='未开始计时'
        self.lasted=[]
        self.begin=0
        self.end=0

    def __str__(self):
        return self.prompt

    __repr__=__str__

    def __add__(self, other):
        prompt='一共运行了'
        result=[]
        for index in range(6):
            result.append(self.lasted[index]+other.lasted[index])
            if result[index]:
                prompt+=(str(result[index])+self.unit[index])
        return prompt

    def start(self):
        self.begin=t.localtime()
        self.prompt='请先调用stop()停止计时'
        print('计时开始...')

    def stop(self):
        self.end=t.localtime()
        if not self.begin:
            print('请先调用start()进行计时')
        else:
            self._calc()
            print('停止计时...')

    def _calc(self):
        self.lasted=[]
        self.prompt='总计运行了'
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:
                self.prompt+=str(self.lasted[index]) + self.unit[index]
