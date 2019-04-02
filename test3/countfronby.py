class CountFronBy:
    def __init__(self, val: int ,incr: int) -> None:
        self.val = val
        self.incr = incr
    def __repr__(self) -> str:
        return str(self.val)
    def increase(self) -> None:
        self.val += self.incr

