import numpy as np
#import driftcardslib.time as dctime

# GPSINS(1) - Latitude (Decimal Degrees)
# GPSINS(2) - Longitude (Decimal Degrees)
# GPSINS(3) - Altitude (meters)
# GPSINS(4) - Roll (degrees)
# GPSINS(5) - Pitch (degrees)
# GPSINS(6) - Heading (degrees)
# GPSINS(7) - GPS millisecond of the week

def read_INS_field(exp,field):
 out = []

 if not (field in ['lat','lon','pitch','roll','heading','alt','time']): 
  print str(field) + ' not valid'
  print 'input field has to be one of [lat,lon,pitch,roll,heading,alt,time]'
 else:
  if field == 'lat':            fid = 1
  elif field == 'lon':          fid = 3
  elif field == 'alt':          fid = 5
  elif field == 'roll':         fid = 7
  elif field == 'pitch':        fid = 8
  elif field == 'heading':      fid = 9
  else:                         fid = 10
 
  filename = '/home/jmensa/LASER/scripts_LASER/P3/INS/'+exp+'_INS_NMEA_LOG.txt'
  f = open(filename,'r')
  INS = f.readlines()
  f.close()
  
  nimg = len(INS) # number of images
  for n in range(nimg):
   INSt = INS[n].split(',')
   out.append(float(INSt[fid]))

 return np.asarray(out) 


def read_INS_all(filename):
 out = []

 f = open(filename,'r') 
 INS = f.readlines()
 f.close()

 nimg = len(INS) # number of images
 
 for n in range(nimg):
  INSt = INS[n].split(',')
  out.append((float(INSt[1]),float(INSt[3]),float(INSt[5]),float(INSt[7]),float(INSt[8]),float(INSt[9]),float(INSt[10])))

 return np.asarray(out)

def read_INS_frame(filename):
 # read INS data for XY positions in filename
 f = open(filename,'rb')
 INS = f.readline().split(',')
 f.close()
 return INS

def write_INS_frame(INS_all,time_INS,time_frame,filename):
 INS_frame = INS_all[np.where(time_INS >= time_frame)[0][0],:]
 f = open(filename,'wb') 
 f.write(str(INS_frame[0])+','+str(INS_frame[1])+','+str(INS_frame[2])+','+str(INS_frame[3])+','+str(INS_frame[4])+','+str(INS_frame[5])+','+str(time_frame))
 f.close()
 return

