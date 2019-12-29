class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        m=0
        
        for x in range(0,len(a)):
            for y in range(0,len(a)):
               absl=abs(a[x]-a[y])
               if absl > m:
                   m= absl
        self.maximumDifference = m
       
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
