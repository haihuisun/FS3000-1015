from time import sleep
from pinpong.board import Board,I2C
import time

Board("uno").begin()  
FS3000_1015 = I2C()

while True:
  data_buf = FS3000_1015.readfrom(0x28,5)#Read 6 bytes of data from the address 0x44 of the SHT40
  checksum = data_buf[0]
  sum = data_buf[1] + data_buf[2]
  if(checksum + sum == 256):
    print('valid')
  else:
    print('unvalid')
  hex_string = "0x" + str(sum)
  output = int(hex_string, 16)
  print('output',output)
  if(output < 409)  :
    print("air velocity: 0 m/sec")
  elif(1203 <= output < 1597):
    print("air velocity: 2 m/sec")
  time.sleep(1)#Wait for 0.1 second
  

