import numpy as np

def princax(x,y):
    #
    #   Input:  x, y  = particles location
    #
    #   Output: theta = angle of maximum variance, (east == 0, north=90)
    #           maj   = major axis of principal ellipse
    #           min   = minor axis of principal ellipse
    #           wr    = rotated time series, where real(wr) is aligned
    #                   with the major axis.

    # Covariance matrix 
    cv = np.cov(x,y)

    #  Find direction of maximum variance
    theta = 0.5*np.arctan2(2*cv[1,0],(cv[0,0]-cv[1,1]))

    #  Find major and minor axis amplitudes
    term1 = (cv[0,0]+cv[1,1])
    term2 = np.sqrt((cv[0,0]-cv[1,1])**2 + 4*cv[1,0]**2)

    maj   = np.sqrt(.5*(term1+term2))
    min   = np.sqrt(.5*(term1-term2))

    #  Rotate into principal ellipse orientation
    # wr = w*np.exp(-1j*theta) 
    theta   = theta*180./np.pi

    return theta,maj,min

def writeDisp(fileout,t_t,a_t,b_t):
 a_t = np.asarray(a_t)
 b_t = np.asarray(b_t)
 t_t = np.asarray(t_t)
 f = open(fileout, 'wb')
 for t in range(len(a_t)):
  f.write(str(t_t[t])+','+str(a_t[t])+','+str(b_t[t])+'\n')
 f.close()
 return

import csv

def readDisp(filename):
 a_t = []
 b_t = []
 t_t = []

 f = open(filename, 'rb')
 reader = csv.reader(f)

 for row in reader:
  t_t.append(float(row[0]))
  a_t.append(float(row[1]))
  b_t.append(float(row[2]))

 f.close()

 t_t = np.asarray(t_t)
 a_t = np.asarray(a_t)
 b_t = np.asarray(b_t)

 return t_t,a_t,b_t

def readDiffOkubo(filename):
 # Okubo's data
 f = open(filename,'r')
 data = [line.split() for line in f.readlines()]
 x_okubo = []
 y_okubo = []
 for line in data:
     x_okubo.append(np.float(line[0]))
     y_okubo.append(np.float(line[1]))
 f.close()
 x_okubo = np.array(x_okubo)
 y_okubo = np.array(y_okubo)
 return x_okubo,y_okubo

def readDiffGLAD(filename):
 # drew's data
 f = open(filename,'r')
 data = [line.split() for line in f.readlines()]
 x_drew = []
 y_drew = []
 for line in data:
     x_drew.append(np.float(line[0]))
     y_drew.append(np.float(line[1]))
 f.close()
 x_drew = np.array(x_drew)*1E5
 y_drew = np.array(y_drew)*1E5
 return x_drew,y_drew

# moved to time.py
#def cleanTime(exp,t_i,t_f,t_t):
# # d_i, first image (index) with plates in water
# # d_f, # last time (index) valid for dispersion 
#
# if exp == 'F4':
#  d_i = 30
#  d_f = 180
# elif exp == 'F8':
#  d_i = int(np.where(t_t/15 == t_i)[0]) 
#  d_f = int(np.where(t_t/15 == t_f)[0]) 
# elif exp == 'F10':
#  d_i = int(np.where(t_t/15 == t_i)[0]) 
#  d_f = int(np.where(t_t/15 == t_f)[0]) 
#
# return d_i,d_f
