import numpy as np

def glare(frame,thrs):
 #rgb -> mask
 size = frame.shape
 frame_r = np.reshape(np.flipud(frame[:,:,0]),(-1,))
 frame_g = np.reshape(np.flipud(frame[:,:,1]),(-1,))
 frame_b = np.reshape(np.flipud(frame[:,:,2]),(-1,))

 #mask_g = abs((frame_r.astype('float')-frame_g.astype('float'))*(frame_r.astype('float')-frame_b.astype('float'))*(frame_g.astype('float')-frame_b.astype('float')))
 mask_g = (frame_r.astype('float')-frame_g.astype('float'))**2*(frame_r.astype('float')-frame_b.astype('float'))**2*(frame_g.astype('float')-frame_b.astype('float'))**2
# mask_g = ((frame_r.astype('float')-frame_b.astype('float'))**2+(frame_g.astype('float')-frame_b.astype('float'))**2+(frame_r.astype('float')-frame_g.astype('float'))**2) 

 delta_s = np.percentile(mask_g,thrs) #99.99 works for F4 and F8, 99.999 for F10

 return np.reshape(mask_g,(size[0],size[1])), delta_s

def color_select(frame,delta_r,delta_g,delta_b,cards_c):
 #rgb -> mask
 size = frame.shape
 frame_r = np.reshape(np.flipud(frame[:,:,0]),(-1,))
 frame_g = np.reshape(np.flipud(frame[:,:,1]),(-1,))
 frame_b = np.reshape(np.flipud(frame[:,:,2]),(-1,))

 frame_r[np.where((frame_r <= cards_c[0]+delta_r) & (frame_r >= cards_c[0]-delta_r))] = 1
 frame_g[np.where((frame_g <= cards_c[1]+delta_g) & (frame_g >= cards_c[1]-delta_g))] = 1
 frame_b[np.where((frame_b <= cards_c[2]+delta_b) & (frame_b >= cards_c[2]-delta_b))] = 1

 frame_r[np.where(frame_r != 1)] = 0
 frame_g[np.where(frame_g != 1)] = 0
 frame_b[np.where(frame_b != 1)] = 0

 mask = np.reshape(frame_b*frame_r*frame_g,(size[0],size[1]))
 return mask

