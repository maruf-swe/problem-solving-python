class Difference:

    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        sorted_elements = sorted(self.__elements)
        self.maximumDifference = sorted_elements[-1] - sorted_elements[0]


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
