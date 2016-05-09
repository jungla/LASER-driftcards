from math import modf
import datetime
from PIL import Image

def timeframe(filename):
 frame = Image.open(filename)
 exif_time = datetime.datetime.strptime(str(frame._getexif()[306]),'%Y:%m:%d %H:%M:%S')
 time_frame = datetime.date.toordinal(exif_time) + datetime.timedelta(days=0, hours=exif_time.hour, minutes=exif_time.minute, seconds=exif_time.second).total_seconds()/86400.
 return time_frame

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


