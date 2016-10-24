import numpy as np

'''
Read and write subroutines

'''
def readXY(filename):
 # read XY positions in filename
 f = open(filename,'rb')
 XY = f.readlines()
 f.close()

 X = []
 Y = []

 for n in range(len(XY)):
  X.append(float(XY[n].split(',')[0]))
  Y.append(float(XY[n].split(',')[1]))

 return np.asarray(X),np.asarray(Y)

# moved to INS
#def readXY_INS(filename):
# # read INS data for XY positions in filename
# f = open(filename,'rb')
# INS = f.readline().split(',')
# f.close()
# return INS

def writeXY(filename,(X,Y)):
 f = open(filename,'wb')
 for t in range(len(X)):
  f.write(str(X[t])+','+str(Y[t])+'\n')
 f.close()
