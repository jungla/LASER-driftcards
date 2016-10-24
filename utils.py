import numpy as np

def digit(day,n):
 lday  = str(day)
 while (len(lday) < n):
  lday = '0'+lday
 return lday

def moving_average(a, n) :
    ret = np.cumsum(a,0)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

def smooth(x,beta):
 """ kaiser window smoothing """
 window_len=11
 # extending the data at beginning and at the end
 # to apply the window at the borders
 s = np.r_[x[window_len-1:0:-1],x,x[-1:-window_len:-1]]
 w = np.kaiser(window_len,beta)
 y = np.convolve(w/w.sum(),s,mode='valid')
 return y[5:len(y)-5]

