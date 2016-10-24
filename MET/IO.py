import numpy as np
import csv

def write_met_frame(met_all,time_met,time_frame,filename):
 met_frame = met_all[np.where(time_met >= time_frame)[0][0],:]
 f = open(filename,'wb')
 f.write(str(met_frame[1])+','+str(met_frame[2])+','+str(met_frame[3])+','+str(met_frame[4])+','+str(met_frame[5])+','+str(met_frame[6])+','+str(met_frame[7])+','+str(met_frame[8])+','+str(met_frame[9])+','+str(time_frame))
 f.close()
 return

def read_met_all(filename):
 MET = []
 with open(filename, 'rb') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',')
  for row in spamreader:
   MET.append(row[:])
 return np.asarray(MET).astype(float)

def read_met_frame(filename):
 return
