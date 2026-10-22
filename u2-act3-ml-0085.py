# Ricardo Lopez NC 0085
import numpy as np

n0085=np.array([10, 20, 30, 40, 50])
print(n0085)
print(n0085[0])
print(n0085[3])
print(n0085[-1])
print(n0085[-2])
print("----------------------------")

n0085=np.array((
    [10,20,30],
    [40,50,60]
    ))
print(n0085[0,  0])
print(n0085[1,  2])
print(n0085[-1,  -1])
print(n0085[-2,  -2])
print("----------------------------")

n0085=np.array(([
    [10, 20, 30],
    [40, 50, 60]
 ],
 [
    [70, 80, 90],
    [100, 110, 120]
 ]
    ))
print(n0085)
print(n0085[0 ,0 ,0])
print(n0085[1 ,1 ,2])
print("Ricardo Lope NC 0085 ")