import numpy as np

a1=np.array([[1,2,3,4],[5,6,7,8],[11,12,13,14],[2,3,4,5]])
print(a1)
print(a1[:,1])
temp=a1[:,0:2]
print(temp)

print(temp.reshape(1,-1).T)


class test():
    a=None;
    def __init__(self):
        b=1;
        a=2;
        self.c=3;
    def pr(self):
        print(b);


test_1=test();
test_1.pr();
