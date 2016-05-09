import numpy as np

def tiling(frame,delta):
 # reduce resolution simply reducing
 # simply average over tile. Ideally the tile should be a moving circle

 size = frame.shape
 frame_t = np.zeros((size[0]/delta+1,size[1]/delta+1))

 for i in range(0,size[0]-delta,delta):
  for j in range(0,size[1]-delta,delta):
   frame_t[i/delta,j/delta] = np.mean(frame[i:i+delta,j:j+delta])
 
 for i in range(size[0]-delta,size[0]):
  for j in range(0,size[1]-delta,delta):
   frame_t[-1,j/delta] = np.mean(frame[i,j:j+delta])
 
 for i in range(0,size[0]-delta,delta):
  for j in range(size[1]-delta,size[1]):
   frame_t[i/delta,-1] = np.mean(frame[i:i+delta,j])

 Xm,Ym = np.meshgrid(range(frame_t.shape[1]),range(frame_t.shape[0]))
 return Xm,Ym,frame_t


def masking(mask,delta_s):
 size = mask.shape
 X,Y = np.meshgrid(range(size[1]),range(size[0]))

 X = np.reshape(X,(-1,))
 Y = np.reshape(Y,(-1,))

 mask = np.reshape(mask,(-1,))

 X = X[np.where(mask > delta_s)]
 Y = Y[np.where(mask > delta_s)]
 return X,Y
