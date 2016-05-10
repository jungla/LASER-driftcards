def expTime(exp):
 # t_i, starting time (index) 
 # t_f, ending time (index)
 # noise_list, list of noisy frames (index) 

 if exp == 'F4':
  d_i = 30
  d_f = 180
  t_i = 23
 elif exp == 'F8':
  t_i = 26
  t_f = 821
  noise_list = range(113,127) + [560,736,737,738,739,740,741,742,743,744,745,746,747] + range(774,804)
 elif exp == 'F10':
  t_i = 45
  t_f = 460
  noise_list = [57,58,59,70,71,72,74]  + range(84,89) + [95,96,98,107,108,109,116,117,118,127,141,149,159] + range(161,169) + [183,203,310,333,380,382,502]
 return t_i,t_f,noise_list
