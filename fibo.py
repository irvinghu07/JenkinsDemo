class Fibo:

    def __init__(self, b: int):
        self.boarder = b

    def cal_fibo(self):
        return self.fibonacci(self.boarder)

    def fibonacci(self, n: int) -> int:
        if 0 <= n < 2:
            return n
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)
