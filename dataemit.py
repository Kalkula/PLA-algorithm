from numpy import random
import numpy as np

#输入w=[w0,w1,w2],计算h(x)
m=input('the number of \'+\'=')
n=input('the number of \'-\'=')
w=np.array(eval(input('w=')))

'''print(type(w))'''
with open('train.txt','w') as f:
    f.write('')

def k():
    l=np.array([1,random.uniform(-200,200),random.uniform(-200,200)],dtype=float)
    return l


#按照标记产生随机x点，输出到train.txt
i=1
j=1
while i<=int(m):    
    x=k()
    h=np.dot(w.T,x)
    x1=round(x[1],1)
    x2=round(x[2],1)
    if h>0:
        with open('train.txt','a') as f:
            f.write(str(x1))
            f.write(' ')
            f.write(str(x2))
            f.write(' +1\n')  
            i+=1
    elif h<=0:
        continue    
    if i>int(m):
        break
    
while j<=int(n):
    x=k()
    h=np.dot(w.T,x)
    x1=round(x[1],1)
    x2=round(x[2],1)
    if h<0:
        with open('train.txt','a') as f:
            f.write(str(x1))
            f.write(' ')
            f.write(str(x2))
            f.write(' -1\n')  
            j+=1        
    elif h>=0:
        continue 
    if j>int(n):
        break  




     