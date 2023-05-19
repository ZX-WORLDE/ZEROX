#<\>!python3.11
#-------------------Dont Edit This Script-----------------#
import os
from platform import architecture
os.system('xdg-open https://www.facebook.com/groups/1820604221328119/?ref=share&mibextid=NSMWBT')
if architecture()[0]=='64bit':os.system('git pull;chmod +x Mahadi;./Mahadi')
 
#elif architecture()[0]=='32bit':os.system('git pull;chmod +x Sefat;./Sefat')
 
else:exit('\033[1;31m\n Sorry you device 32 bit not support ')
