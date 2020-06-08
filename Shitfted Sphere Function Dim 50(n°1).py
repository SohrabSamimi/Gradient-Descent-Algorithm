

import numpy as np
import random
import math
import time
import matplotlib.pyplot as plt

def square(x):
    sum=0
    for i in range(len(x)):
        sum=sum+(x[i])**2
    return sum
    

#We define the objective function:
def shifted_sphere(x):
    my_sum=square(x-shift)
    return my_sum-450  

#Initializing the shift randomly:
D=50
shift=np.random.uniform(-100,100,D)
shift




#definition of the gradient of a function 'func' at point x:
def grad(func,x,h=1e-5):
    n=len(x)
    e=[[0 for l in range(n)] for m in range(n)]
    q=np.zeros(n)
#We define the n basis vectors in R^n:    
    for i in range(n):
        for j in range(n):
            if j==i:
                e[i][j]=1
            else:
                e[i][j]=0           
#We define the l-th partial derivative:            
    for l in range(n):           
        q[l]=(1/h)*(func(np.array(x)+h*np.array(e[l]))-func(np.array(x)))
    return q


t0=time.time()
#We now define the gradient descent algorithm,which returns the optimal solution,
#the number of iterations(represented by the variable counter),and plots the convergence curve:
def grad_desc(func,bound,epsilon,n,lr=0.1):
    x0=np.array([random.uniform(-bound,bound) for i in range(n)])
    grad_func=grad(func,x0)
    norm_grad=math.sqrt(square(grad_func))
    counter=0
    a=np.array([])
    #we define hereafter the gradient descent algorithm:
    while norm_grad>epsilon:
        x0=x0-lr*grad_func
        grad_func=grad(func,x0)
        norm_grad=math.sqrt(square(grad_func))
        #we now count the iterations:
        counter+=1
        a=np.append(a,func(x0))
        #we plot the convergence curve:
        plt.plot(a)
        plt.xlabel("Iterations(time)")
        plt.ylabel("Fitness")
    return np.array([x0,counter])
  
t1=time.time()
print("The computational time is: ",t1-t0)    

m=grad_desc(shifted_sphere,100,0.01,D)
#We print the solution,the number of iterations and the fitness value:
print("Solution of this minimization problem: ",m[0])
print("Number of iterations: ",m[1])
print("Fitness value: ",shifted_sphere(m[0]))
#Convergence curve:







    
