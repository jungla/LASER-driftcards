import csv
import datetime
import numpy as np

def read_GPS(filename):
 lat = []
 lon = []
 time = []
 date = []
 with open(filename, 'rb') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
  for row in spamreader:
#   if row[0] == '$GPGLL' and row[1] != '' and row[3] != '':
#    lat.append(row[1])
#    lon.append(row[3])
#    time.append(row[5])
   if row[0] == '$GPRMC' and row[1] != '' and row[3] != '':
    lat.append(row[3])
    lon.append(row[5])
    time.append(row[1])
#   elif row[0] != '$GPGLL' and  row[0]=='$GPGGA' and row[2] != '' and row[4] != '':
#    lat.append(row[2])
#    lon.append(row[4])
#    time.append(row[1])

 return lat,lon,time

def latlonGPS(XGPS,YGPS,GPS_time,frame_time,filename_GPS):
 lat = float(YGPS[np.where(GPS_time>=frame_time)[0][0]])
 lon = float(XGPS[np.where(GPS_time>=frame_time)[0][0]])
 return lat, lon

def timeGPS(timeM8,filename_GPS):
 GPS_time = datetime.datetime.strptime(filename_GPS.split('_')[2]+timeM8.split('.')[0],'%Y%m%d%H%M%S')
 GPS_frame = datetime.date.toordinal(GPS_time) + datetime.timedelta(days=0, hours=GPS_time.hour, minutes=GPS_time.minute, seconds=GPS_time.second, microseconds=int(timeM8.split('.')[1])).total_seconds()/86400.
 return GPS_frame

#def find_GPS_frame():
