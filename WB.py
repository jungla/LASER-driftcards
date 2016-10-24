import csv
import numpy as np

# wave buoys files contains the following records separated by spaces

%int(Month)/%int(Day)/%int(Year)
%int(Hours):%int(Minutes):%float(Seconds)
%float(OrientQuatX),%float(OrientQuatY),%float(OrientQuatZ),%float(OrientQuatW)
%float(CorrectedAccelX),%float(CorrectedAccelY),%float(CorrectedAccelZ)
%float(CorrectedCompassX),%float(CorrectedCompassY),%float(CorrectedCompassZ)
%float(CorrectedGyroX),%float(CorrectedGyroY),%float(CorrectedGyroZ)
%float(LinearAccelX),%float(LinearAccelY),%float(LinearAccelZ)"

def read_WB(filename):
 f = open(filename,'r')
 f.close()
 return


