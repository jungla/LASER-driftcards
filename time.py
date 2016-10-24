from math import modf
import datetime
from PIL import Image
import numpy as np

def timeframe(filename):
 frame = Image.open(filename)
 exif_time = datetime.datetime.strptime(str(frame._getexif()[306]),'%Y:%m:%d %H:%M:%S')
 time_frame = datetime.date.toordinal(exif_time) + datetime.timedelta(days=0, hours=exif_time.hour, minutes=exif_time.minute, seconds=exif_time.second).total_seconds()/86400.
 return time_frame

#def find_INS_frame(INS_all,time_INS,time_frame):
# INS_frame = INS_all[np.where(time_INS >= time_frame)[0][0],:]
# return INS_frame

def timeGap(exp):
 if exp == 'F4':
  Sunday = datetime.date(2016,1,24)
  shift = 7
 elif exp == 'F8':
  Sunday = datetime.date(2016,1,24)
  shift = 2
 elif exp == 'F10':
  Sunday = datetime.date(2016,1,31)
  shift = 2
 elif exp == 'F14':
  Sunday = datetime.date(2016,1,31)
  shift = 0
 return Sunday,shift

def SOW2UTC(time,Sunday,shift):
 return datetime.date.toordinal(Sunday) + (time/1000.)/86400. + shift*3600./86400. -17/86400. #  date of the previous Sunday + time + offset + offset 

def dddsss2s(ds):
 #
 # convert time from serial date time to seconds

 sec = []

 for d in ds:
  dddsss = modf(d)
  sec.append(dddsss[0]*86400. + dddsss[1]*86400.)

 return np.asarray(sec)

def cleanTime(exp,t_i,t_f,t_t):
 # d_i, first image (index) with plates in water
 # d_f, # last time (index) valid for dispersion 

 if exp == 'F4':
  d_i = 30
  d_f = 180
 elif exp == 'F8':
  d_i = int(np.where(t_t/15 == t_i)[0])
  d_f = int(np.where(t_t/15 == t_f)[0])
 elif exp == 'F10':
  d_i = int(np.where(t_t/15 == t_i)[0])
  d_f = int(np.where(t_t/15 == t_f)[0])

 return d_i,d_f
