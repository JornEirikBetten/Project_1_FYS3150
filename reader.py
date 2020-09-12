import matplotlib.pyplot as plt
import numpy as np

def max_test(a): 
    max_value = 0.0
    for i in range(len(a)-1):
        if (a[i+1]**2>max_value**2):
            max_value = a[i+1]
    return max_value

def file_reader(filename): 
    f = open(filename,'r')
    lines = f.readlines()
    x = []
    u = []
    rel_elog10 = []
    for line in lines: 
        data = line.split(',')
        x.append(data[0])
        u.append(data[1])
        rel_elog10.append(data[2])
    f.close()
    for i in range(len(x)): 
        x[i] = x[i].strip()
        x[i] = float(x[i])
        u[i] = u[i].strip()
        u[i] = float(u[i])
        rel_elog10[i] = rel_elog10[i].strip()
        rel_elog10[i] = float(rel_elog10[i])
    rel_elog10[0] = 0.0
    return x, u, rel_elog10
x1, u1, rel1 = file_reader("gc1.txt")
x2, u2, rel2 = file_reader("gc2.txt")
x3, u3, rel3 = file_reader("gc3.txt")
x4, u4, rel4 = file_reader("gc4.txt")
x5, u5, rel5 = file_reader("gc5.txt")
x6, u6, rel6 = file_reader("gc6.txt")
x7, u7, rel7 = file_reader("gc7.txt")
x8, u8, rel8 = file_reader("gc8.txt")

e1 = max_test(rel1)
e2 = max_test(rel2)
e3 = max_test(rel3)
e4 = max_test(rel4)
e5 = max_test(rel5)
e6 = max_test(rel6)
e7 = max_test(rel7)
e8 = max_test(rel8)
plt.scatter([1,2,3,4,5,6,7,8],[e1,e2,e3,e4,e5,e6,e7,e8])
plt.xlabel('i-values for n=10^i')
plt.ylabel('value of magnitude of relative error, in 10^(value)')
plt.show()
plt.figure(figsize=(8,8))
plt.plot(x1, u1, 'b')
plt.plot(x2, u2, 'g')
plt.plot(x3, u3, 'r')
plt.plot(x4, u4, 'y')
plt.plot(x5, u5, 'pink')
plt.plot(x6, u6, 'indigo')
plt.plot(x7, u7, 'orange')
plt.plot(x8, u8, 'purple')
plt.xlabel('x-values')
plt.ylabel('values of calculated u')
