import numpy as np
#print(np.__version__)
#print(dir(np))
#print(help(np.where))

#t=(4,)
#print(type(t))


A=np.array([[1,2,3],[4,5,6]])
#print(A)
#print(np.reshape(A,(3,2)))
#print(np.reshape(A,(1,-1)))
#print(np.reshape(A,(-1,1)))

x=np.array([1,2,3])
#print(x)

#print(x[:,None])

#y=np.array([[1,2,3],[4,5,6]])       #tedade bo'd ro afzayesh dade)
#print(y)
#print(y[:,None])

#print(y)
#5print(y[:,np.newaxis])


#ARRAY DIMENSION

#print(x)
#print(x.ndim)
#print(A)
#print(A.ndim)


#print(A.dtype)


A=np.array([[1,2,3],[4,5,6]]).astype(np.float64)
print(A)
print(A.dtype)


x=np.arange(1,20,step=3)
print("x=",x)
























