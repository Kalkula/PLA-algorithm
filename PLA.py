import matplotlib.pyplot as plt
import numpy as np
import time as tm

#count the running time usage
t1=tm.time()

a=np.loadtxt('train.txt')
#delete the label
b=a[:,:2]

numrows=b.shape[0]
x0=np.ones((numrows,1))
x=np.hstack((b,x0))
numcolumns=x.shape[1]

w=np.zeros((1,numcolumns))
'''print(w.T)
print(type(x))
'''


separated=False
i=0
'''c=np.dot(w.T,x[i])
print(c.type)
print(x[i])
print(x.shape)
the shape of x[i] is (4,)?????????'''
#recursion use pla
while not separated and i<numrows:
    if a[i][-1]*np.dot(w,x[i,:])<=0:
        w=w+a[i][-1]*x[i,:]
        separated=False
        i=0
    else:
        i+=1

#count the running time usage
t2=tm.time()
timeusage=float(t2-t1)
print('time usage=',timeusage)

#write down the learned weight    
w3=str(w[:]).replace('[','').replace(']','')
with open('PLAtrain.txt','w') as f:
    f.write('<%s>\n'%w3)


#plot
fig=plt.figure()  
plt.title('linearSeparatabledata')
ax=fig.add_subplot(111)
plt.xlabel('X1')
plt.ylabel('X2')
x1=a[:,0]
x2=a[:,1]
labels=a[:,2]
index1=np.where(a[:,2]==1)
index2=np.where(a[:,2]==-1)
p1=ax.scatter(x[index1,0],x[index1,1],marker='o',color='b')
p2=ax.scatter(x[index2,0],x[index2,1],marker='x',color='r')
wx=w[0][0]
wy=w[0][1]
wann=ax.annotate(s='w(learned)',xytext=(-wx,-wy),xy=(wx,wy),
                 size=10,arrowprops=dict(arrowstyle='-|>'))
#plot the separate line
p=np.arange(-200,200)
q=(-1-wx*p)/wy
lineseparate=ax.add_line(plt.Line2D(p, q, color='g'))

plt.savefig("pla.png", dpi=120)     
plt.show()    











  