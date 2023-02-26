class Fraction:
    def __init__(self,a,b):
        self.__a=a
        self.__b=b
    def __str__(self):
        return "{}/{}".format(self.__a,self.__b)

    def __add__(self, other):
        k = self.__a * other.__b + self.__b * other.__a
        l = self.__b * other.__b
        return "{}/{}".format(k, l)
    def __sub__(self, other):
        k = self.__a * other.__b - self.__b * other.__a
        l = self.__b * other.__b
        return "{}/{}".format(k, l)
    def __mul__(self, other):
        k = self.__a * other.__a
        l = self.__b * other.__b
        return "{}/{}".format(k, l)
    def __truediv__(self, other):
        k = self.__a * other.__b + self.__b * other.__a
        l = self.__b * other.__b
        return "{}/{}".format(k, l)
i=Fraction(2,3)
j=Fraction(4,5)
print(i+j)
