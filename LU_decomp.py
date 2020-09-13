import matplotlib.pyplot as plt
import scipy
import numpy as np
import scipy.linalg
n = 10
h = 1.0/n
A = np.zeros((n, n)) #Setting up matrix A
A[n-1, n-1] = 2
x = np.zeros(n)
for i in range(len(A[0])-1): 
    A[i, i] = -2.
    A[i, i+1] = 1.
    A[i+1, i] = 1.
    x[i] = i*h
def sec_der(x): # Second derivate of u(x)
    return (-1.0)*h**2*100*np.exp(-10*x)

g = np.zeros(n)
for i in range(n): 
    g[i] = sec_der(i*h)
import time
data = []
for l in range(50):
    
    start = time.perf_counter()
    solution = scipy.linalg.solve(A,g) #Solving matrix A using a solver
    finish = time.perf_counter()
    timer = finish-start
    timer = str(timer)
    data.append(timer)
f = open('time.txt', 'w')
for i in range(len(data)): #Writing the timer to a file
    f.write(data[i] + ',') 

f.close()
plt.figure(figsize=(8,8)) #Plotting the approximation and the exact solution
plt.plot(x, solution)
plt.plot(x, exact(x))
plt.show()

## 
def filereader(filename): # Opening file to read data again. 
    f = open(filename, 'r')
    data = f.read()
    data = data.split(',')
    for i in range(len(data)-1): 
        data[i] = float(data[i])
    return data
data = filereader('time.txt')
print(data)
average = 0
for i in range(len(data)-1): 
    average =average+ data[i]
average = average/(len(data)-1.0)
print(average)






