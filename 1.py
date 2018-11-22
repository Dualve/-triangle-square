from math import fabs
x1,y1,x2,y2,x3,y3 = map(int,input().split())
a = (0.5*(fabs(((x1-x3)*(y2-y3))-((x2-x3)*(y1-y3)))))
if a != int(a):
    print(a)
else:
    print(int(a))
