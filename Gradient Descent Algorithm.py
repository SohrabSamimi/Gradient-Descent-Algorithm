

import numpy as np
import random
import math

def square(x):
    sum=0
    for i in range(len(x)):
        sum=sum+(x[i])**2
    return sum
    

#We defined the shifted sphere function,shifted by the vector o,which we initialize to have 
#all its components equal to 1 here
def shifted_sphere(x):
    sum=0
    for i in range(len(x)):
        sum=sum+(x[i]-o[i])**2
    sum1=sum-450
    return sum1


o=[1 for i in range(2)]
shifted_sphere([1,1])



#definition of the gradient of a function 'func' at point x:
def grad(func,x,h=1e-5):
    n=len(x)
    e=[[0 for l in range(n)] for m in range(n)]
    q=np.zeros(n)
    iter=0
#We here define the n basis vectors in R^n:    
    for i in range(n):
        for j in range(n):
            if j==i:
                e[i][j]=1
            else:
                e[i][j]=0           
#We here define the l-th partial derivative:            
    for l in range(n):           
        q[l]=(1/h)*(func(np.array(x)+h*np.array(e[l]))-func(np.array(x)))
    return q

np.empty(2)
x=[]
l=np.append(x,1)
l
#We now define the gradient descent algorithm:
def grad_desc(func,bound,epsilon,n,lr=0.5):
    x0=np.array([random.uniform(-bound,bound) for i in range(n)])
    grad_func=grad(func,x0)
    norm_grad=math.sqrt(square(grad_func))
    counter=0
    my_list=[]
    while norm_grad>epsilon:
        x0=x0-lr*grad_func
        grad_func=grad(func,x0)
        norm_grad=math.sqrt(square(grad_func))
    return x0
    

#We apply GDA on the square function:
m=grad_desc(shifted_sphere,10,0.01,2)   
print(m)
#As we see the solution is very close to the vector o,which is the theoretical solution. 
#Let us compute the value of the function at this minimum:
print(shifted_sphere(m))
