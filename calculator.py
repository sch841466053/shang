"""
auth:尚春洪
Date:2018/09/08
Descripe:实现简单的计算功能
"""


class Calculator:
    """
     实现两个数的加减乘除
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    # def mul(self):
    #     return self.a * self.b

    def div(self):
        return self.a / self.b
