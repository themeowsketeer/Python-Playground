import math
result1=[]
result2=[]
for t in range(0,5):
    h=(40*t*(1/2))-(0.5*10*(t^2))
    v=math.sqrt((40^2)-2*40*10*(1/2)+((10^2)*(t^2)))
    result1.append(h)
    result2.append(v)
print(result1)
print(result2)