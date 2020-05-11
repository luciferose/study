class CountList:
    def __init__(self,*args):
        self.values=[x for x in args]
        self.count=[]

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __delitem__(self, key):
        del self.values[key]

    def __setitem__(self, key, value):
        self.values[key]=value