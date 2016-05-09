import numpy as np

def dan_map_image(angx,angy,roll,pitch,hdg,elev):
 # 
 # [xr,yr,path] = dan_map_image(angx,angy,roll,pitch,hdg,elev)
 #
 # This function computes distance offsets for pixel locations and path
 # lengths for each pixel to the sensor. Assumes X-dir of camera
 # perpendicular to longitudinal axis of platform (if an aircraft, parallel
 # to the wings)
 #
 # INPUTS:
 # angx, angy - Base Angles
 # roll - measured by GPS-INS
 # pitch - measured by GPS-INS
 # hdg - heading measured by GPS-INS
 # elev - elevation measured by GPS-INS
 #
 # OUTPUTS:
 # xr - offset distance in X (camera X) - units meters
 # yr - offset distance in Y (camera Y) - units meters
 # path - path length of light from each pixel to sensor
 #
 # Adapted from map.m by J. Molemaker
 #
 # Last Modified: 8 October 2015
 ###########################################################################

 d2r = np.pi/180

 roll = roll*d2r
 pitch = pitch*d2r
 hdg = hdg*d2r

 axc = angx + roll
 ayc = angy + pitch

 xc = np.tan(axc)*elev/np.cos(ayc)
 yc = np.tan(ayc)*elev/np.cos(axc)

# path = np.sqrt(elev**2+xc**2 + yc**2)

 sin_hdg = np.sin(hdg)
 cos_hdg = np.cos(hdg)

 xr = cos_hdg*xc + sin_hdg*yc
 yr =-sin_hdg*xc + cos_hdg*yc

 return xr,yr

def dan_comp_ang(foclen,PixDim):
 '''
  [angx,angy] = dan_comp_ang(foclen,PixDim)
 
  This function computes base image angles in radians using the
  focal length of the lens and the pixel resolution, and assuming a
  full-frame 36 x 24 mm sensor
 
  INPUTS:
  foclen - focal length of the lens units = mm
  PixDim - Pixel resolution of sensor - X x Y
 
  OUTPUTS:
  [angx,angy] = Image base angles used for direct rectification
 
  Adapted from comp_ang.m by J. Molemaker
 
  Last Modified: 8 October 2015
 '''

 delX = 2*np.arctan(36./(foclen*2)) # FOV angle X in rad
 delY = 2*np.arctan(24./(foclen*2)) # FOV angle Y in rad

 nx = PixDim[0]
 ny = PixDim[1]

 x2  = -delX/2 + delX*np.linspace(0.5,nx-0.5,nx)/nx
 y2  = -delY/2 + delY*np.linspace(0.5,ny-0.5,ny)/ny
 [x2,y2] = np.meshgrid(x2,y2)

 ax2 = np.arctan(x2)
 ay2 = np.arctan(y2)

 for it in range(6): # WHY???
     axn = np.arctan(np.cos(ay2)*x2)
     ayn = np.arctan(np.cos(ax2)*y2)
     ax2 = axn
     ay2 = ayn

 angx = ax2.T
 angy = ay2.T

 return angx, angy


def comp_ang_XY(foclen,PixDim,X,Y):
 '''
  [angx,angy] = dan_comp_ang(foclen,PixDim)
 
  This function computes base image angles in radians using the
  focal length of the lens and the pixel resolution, and assuming a
  full-frame 36 x 24 mm sensor
 
  INPUTS:
  foclen - focal length of the lens units = mm
  PixDim - Pixel resolution of sensor - X x Y
 
  OUTPUTS:
  [angx,angy] = Image base angles used for direct rectification
 
  Adapted from comp_ang.m by J. Molemaker
 
  Last Modified: 8 October 2015

 '''

 delX = 2*np.arctan(36./(foclen*2)) # FOV angle X in rad
 delY = 2*np.arctan(24./(foclen*2)) # FOV angle Y in rad

 nx = PixDim[0]
 ny = PixDim[1]

 x2 = delX/2 + delX*(X-nx)/nx
 y2 = delY/2 + delY*(Y-ny)/ny

 ax2 = np.arctan(x2)
 ay2 = np.arctan(y2)

 for it in range(6): # WHY???
     axn = np.arctan(np.cos(ay2)*x2)
     ayn = np.arctan(np.cos(ax2)*y2)
     ax2 = axn
     ay2 = ayn

 angx = ax2.T
 angy = ay2.T

 return angx, angy
